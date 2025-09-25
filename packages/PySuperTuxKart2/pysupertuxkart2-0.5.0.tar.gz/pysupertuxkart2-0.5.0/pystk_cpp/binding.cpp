#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <pybind11/embed.h>
#include <memory>
#include <string>
#include <sstream>
#include <vector>
#include "pickle.hpp"
#include "pystk.hpp"
#include "state.hpp"
#include "simulation.hpp"
#include "view.hpp"
#include "utils/constants.hpp"
#include "objecttype.hpp"
#include "utils/log.hpp"

#ifdef WIN32
#include <Windows.h>
#endif

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_MAKE_OPAQUE(std::vector<PySTKPlayerConfig>);

void path_and_init(const PySTKGraphicsConfig & config) {
    // Download data if no

    const auto data_dir_env = getenv("SUPERTUXKART_DATADIR");
    if (data_dir_env) 
    {
        // Use environment variable
        PyGlobalEnvironment::init(config, data_dir_env);
    }
    else
    {

        auto locals = py::dict();
        py::exec(R"(
from pathlib import Path
import sys
from tarfile import TarFile
import requests
from platformdirs import user_cache_dir

cachedir = Path(user_cache_dir("PySuperTuxKart2", "bpiwowar"))

cachedir.mkdir(parents=True, exist_ok=True)

VERSION = "1.5-rc2"
FILENAME = f"SuperTuxKart-{VERSION}-src.tar.gz"
SUPERTUXKART_URL = f"https://github.com/supertuxkart/stk-code/releases/download/{VERSION}/{FILENAME}"

ASSETS_DIR= cachedir / VERSION
DOWNLOADED_FILE = ASSETS_DIR / "__downloaded__.txt"

ASSETS_ARCHIVE = cachedir / FILENAME
ASSETS_ARCHIVE_TMP  = cachedir / f"{FILENAME}.tmp"

if not DOWNLOADED_FILE.is_file():
    # Download archive        
    if not ASSETS_ARCHIVE.is_file():
        sys.stderr.write(f"Downloading {SUPERTUXKART_URL}\n")
        with ASSETS_ARCHIVE_TMP.open('wb') as fp, requests.get(SUPERTUXKART_URL, stream=True, allow_redirects=True) as r:
            total_length = r.headers.get('content-length')
            if total_length is None:
                fp.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in r.iter_content(1 << 20):
                    dl += len(data)
                    fp.write(data)
                    done = int(50 * dl / total_length)
                    # sys.stdout.write("\r[%s%s] %3d%%" % ('=' * done, ' ' * (50 - done), 100 * dl / total_length))

        ASSETS_ARCHIVE_TMP.rename(ASSETS_ARCHIVE)
    
    # Decompress
    sys.stderr.write(f"Extracting data from {ASSETS_ARCHIVE}\n")
    ASSETS_DIR.mkdir(exist_ok=True)
    with TarFile.open(ASSETS_ARCHIVE, "r:gz") as tf:
        while tf_info := tf.next():
            tf_path = Path(tf_info.name)
            parents = list(tf_path.parents)
            if len(parents) > 2 and parents[-3].name == "data":
                tf_info.name = tf_path.relative_to(parents[-3])
                tf.extract(tf_info, str(ASSETS_DIR / "data"))

    sys.stderr.write("Cleaning up")
    DOWNLOADED_FILE.write_text("done")
    ASSETS_ARCHIVE.unlink()

ASSETS_DIR = str(ASSETS_DIR)
)", py::globals(), locals);
    
        auto pystk_data = locals["ASSETS_DIR"].cast<std::string>();
        PyGlobalEnvironment::init(config, pystk_data);
    } 
}

PYBIND11_MODULE(pystk2, m) {
    m.doc() = "Python SuperTuxKart interface";
    m.attr("__version__") = std::string(STK_VERSION);
#ifdef SERVER_ONLY
    m.attr("has_graphics") = false;
#else
    m.attr("has_graphics") = true;
#endif  // SERVER_ONLY

    // Adjust the log level
    Log::setLogLevel(Log::LL_FATAL);
    if (getenv("PYSTK_LOG_LEVEL")) {
        std::string ll = getenv("PYSTK_LOG_LEVEL");
        if (ll == "debug") Log::setLogLevel(Log::LL_DEBUG);
        if (ll == "verbose") Log::setLogLevel(Log::LL_VERBOSE);
        if (ll == "info") Log::setLogLevel(Log::LL_INFO);
        if (ll == "warn") Log::setLogLevel(Log::LL_WARN);
        if (ll == "error") Log::setLogLevel(Log::LL_ERROR);
        if (ll == "fatal") Log::setLogLevel(Log::LL_FATAL);
    }
    
    // Define the game state
    defineState(m);

    auto m_simulation = m.def_submodule("simulation", "Module that can handle multiple races (no graphics)");
    defineSimulation(m_simulation);
    
    {
        py::enum_<Log::LogLevel>(m, "LogLevel", "Global logging level")
        .value("debug", Log::LL_DEBUG)
        .value("verbose", Log::LL_VERBOSE)
        .value("info", Log::LL_INFO)
        .value("warn", Log::LL_WARN)
        .value("error", Log::LL_ERROR)
        .value("fatal", Log::LL_FATAL);
        
        m.def("set_log_level", Log::setLogLevel, "Set the global log level");
    }
    
    {
        py::enum_<ObjectType>(m, "ObjectType")
        .value("kart", ObjectType::OT_KART)
        .value("track", ObjectType::OT_TRACK)
        .value("background", ObjectType::OT_BACKGROUND)
        .value("pickup", ObjectType::OT_PICKUP)
        .value("nitro", ObjectType::OT_NITRO)
        .value("bomb", ObjectType::OT_BOMB)
        .value("object", ObjectType::OT_OBJECT)
        .value("projectile", ObjectType::OT_PROJECTILE)
        .value("unknown", ObjectType::OT_UNKNOWN)
        .value("N", ObjectType::NUM_OT, "Number of object types");
        m.def("unknown_debug_name", unknownDebugName);
        m.attr("object_type_shift") = OBJECT_TYPE_SHIFT;
    }
    {
        py::class_<PySTKGraphicsConfig, std::shared_ptr<PySTKGraphicsConfig>> cls(m, "GraphicsConfig", "SuperTuxKart graphics configuration.");
        
        cls.def(py::init<int, int, int, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, int, bool>(), py::arg("screen_width") = 600, py::arg("screen_height") = 400, py::arg("display_adapter") = 0, py::arg("glow") = false, py::arg("") = true, py::arg("") = true, py::arg("") = true, py::arg("") = true, py::arg("particles_effects") = 2, py::arg("animated_characters") = true, py::arg("motionblur") = true, py::arg("mlaa") = true, py::arg("texture_compression") = true, py::arg("ssao") = true, py::arg("degraded_IBL") = false, py::arg("high_definition_textures") = 2 | 1, py::arg("render") = true)
        .def_readwrite("screen_width", &PySTKGraphicsConfig::screen_width, "Width of the rendering surface")
        .def_readwrite("screen_height", &PySTKGraphicsConfig::screen_height, "Height of the rendering surface")
        .def_readwrite("display_adapter", &PySTKGraphicsConfig::display_adapter, "GPU to use (Linux only)")
        .def_readwrite("glow", &PySTKGraphicsConfig::glow, "Enable glow around pickup objects")
        .def_readwrite("bloom", &PySTKGraphicsConfig::bloom, "Enable the bloom effect")
        .def_readwrite("light_shaft", &PySTKGraphicsConfig::light_shaft, "Enable light shafts")
        .def_readwrite("dynamic_lights", &PySTKGraphicsConfig::dynamic_lights, "Enable dynamic lighting")
        .def_readwrite("dof", &PySTKGraphicsConfig::dof, "Depth of field effect")
        .def_readwrite("particles_effects", &PySTKGraphicsConfig::particles_effects, "Particle effect 0 (none) to 2 (full)")
        .def_readwrite("animated_characters", &PySTKGraphicsConfig::animated_characters, "Animate characters")
        .def_readwrite("motionblur", &PySTKGraphicsConfig::motionblur, "Enable motion blur")
        .def_readwrite("mlaa", &PySTKGraphicsConfig::mlaa, "Enable anti-aliasing")
        .def_readwrite("texture_compression", &PySTKGraphicsConfig::texture_compression, "Use texture compression")
        .def_readwrite("ssao", &PySTKGraphicsConfig::ssao, "Enable screen space ambient occlusion")
        .def_readwrite("degraded_IBL", &PySTKGraphicsConfig::degraded_IBL, "Disable specular IBL")
        .def_readwrite("high_definition_textures", &PySTKGraphicsConfig::high_definition_textures, "Enable high definition textures 0 / 2")
        .def_readwrite("render", &PySTKGraphicsConfig::render, "Is rendering enabled?");
        add_pickle(cls);
        
        cls.def_static("hd", &PySTKGraphicsConfig::hd, "High-definitaiton graphics settings");
        cls.def_static("sd", &PySTKGraphicsConfig::sd, "Standard-definition graphics settings");
        cls.def_static("ld", &PySTKGraphicsConfig::ld, "Low-definition graphics settings");
        cls.def_static("none", &PySTKGraphicsConfig::none, "Disable graphics and rendering");
    }
    
    {
        py::class_<PySTKPlayerConfig, std::shared_ptr<PySTKPlayerConfig>> cls(m, "PlayerConfig", "SuperTuxKart player configuration");
    
        py::enum_<PySTKPlayerConfig::Controller>(cls, "Controller")
            .value("PLAYER_CONTROL", PySTKPlayerConfig::PLAYER_CONTROL)
            .value("AI_CONTROL", PySTKPlayerConfig::AI_CONTROL);
        py::enum_<PySTKPlayerConfig::CameraMode>(cls, "CameraMode")
            .value("AUTO", PySTKPlayerConfig::AUTO)
            .value("ON", PySTKPlayerConfig::ON)
            .value("OFF", PySTKPlayerConfig::OFF);
        
        cls
        .def(py::init<const std::string&, const std::string&, PySTKPlayerConfig::Controller, PySTKPlayerConfig::CameraMode, int>(), py::arg("kart")="", py::arg("name")="", py::arg("controller")=PySTKPlayerConfig::PLAYER_CONTROL, py::arg("camera_mode")=PySTKPlayerConfig::AUTO, py::arg("team")=0)
        .def_readwrite("kart", &PySTKPlayerConfig::kart, "Kart type, see list_karts for a list of kart types" )
        .def_readwrite("name", &PySTKPlayerConfig::name, "Name of the player" )
        .def_readwrite("controller", &PySTKPlayerConfig::controller, "Let the player (PLAYER_CONTROL) or AI (AI_CONTROL) drive. The AI ignores actions in step(action)." )
        .def_readwrite("camera_mode", &PySTKPlayerConfig::cameraMode, "Sets the camera on or off. If auto, use a camera for PLAYER_CONTROL only." )
        .def_readwrite("team", &PySTKPlayerConfig::team, "Team of the player 0 or 1" );
        add_pickle(cls);

        py::bind_vector<std::vector<PySTKPlayerConfig>>(m, "VectorPlayerConfig");
    }
    
    {
        py::class_<PySTKRaceConfig, std::shared_ptr<PySTKRaceConfig>> cls(m, "RaceConfig", "SuperTuxKart race configuration.");
    
        py::enum_<PySTKRaceConfig::RaceMode>(cls, "RaceMode")
            .value("NORMAL_RACE", PySTKRaceConfig::RaceMode::NORMAL_RACE)
            .value("TIME_TRIAL", PySTKRaceConfig::RaceMode::TIME_TRIAL)
            .value("FOLLOW_LEADER", PySTKRaceConfig::RaceMode::FOLLOW_LEADER)
            .value("THREE_STRIKES", PySTKRaceConfig::RaceMode::THREE_STRIKES)
            .value("FREE_FOR_ALL", PySTKRaceConfig::RaceMode::FREE_FOR_ALL)
            .value("CAPTURE_THE_FLAG", PySTKRaceConfig::RaceMode::CAPTURE_THE_FLAG)
            .value("SOCCER", PySTKRaceConfig::RaceMode::SOCCER);
        
        cls
        .def(py::init<int,PySTKRaceConfig::RaceMode,std::vector<PySTKPlayerConfig>,std::string,bool,int,int,int,float>(), py::arg("difficulty") = 2, py::arg("mode") = PySTKRaceConfig::NORMAL_RACE, py::arg("players") = std::vector<PySTKPlayerConfig>{{"","",PySTKPlayerConfig::PLAYER_CONTROL}}, py::arg("track") = "", py::arg("reverse") = false, py::arg("laps") = 3, py::arg("seed") = 0, py::arg("num_kart") = 1, py::arg("step_size") = 0.1)
        .def_readwrite("difficulty", &PySTKRaceConfig::difficulty, "Skill of AI players 0..2")
        .def_readwrite("mode", &PySTKRaceConfig::mode, "Specify the type of race")
        .def_readwrite("players", &PySTKRaceConfig::players, "List of all agent players")
        .def_readwrite("track", &PySTKRaceConfig::track, "Track name")
        .def_readwrite("reverse", &PySTKRaceConfig::reverse, "Reverse the track")
        .def_readwrite("laps", &PySTKRaceConfig::laps, "Number of laps the race runs for")
        .def_readwrite("seed", &PySTKRaceConfig::seed, "Random seed")
        .def_readwrite("num_kart", &PySTKRaceConfig::num_kart, "Total number of karts, fill the race with num_kart - len(players) AI karts")
        .def_readwrite("step_size", &PySTKRaceConfig::step_size, "Game time between different step calls")
        .def_readwrite("num_cameras", &PySTKRaceConfig::num_cameras, "Number of cameras to follow the first karts (0 for none)");
        add_pickle(cls);
    }

#ifndef SERVER_ONLY
    {
        py::class_<PySTKRenderData, std::shared_ptr<PySTKRenderData> > cls(m, "RenderData", "SuperTuxKart rendering output");
        cls
       .def_property_readonly("image", [](const PySTKRenderData & rd) { return rd.color_buf_->get(); }, "Color image of the kart (memoryview[uint8] screen_height x screen_width x 3)")
       .def_property_readonly("depth", [](const PySTKRenderData & rd) { return rd.depth_buf_->get(); }, "Depth image of the kart (memoryview[float] screen_height x screen_width)")
       .def_property_readonly("instance", [](const PySTKRenderData & rd) { return rd.instance_buf_->get(); }, "Instance labels (memoryview[uint32] screen_height x screen_width)");
;
//        add_pickle(cls);
    }
#endif  // SERVER_ONLY

    {
        py::class_<PySTKAction, std::shared_ptr<PySTKAction> > cls(m, "Action", "SuperTuxKart action");
        cls
        .def(py::init<float,float,bool,bool,bool,bool,bool>(), py::arg("steer") = 0, py::arg("acceleration") = 0, py::arg("brake") = false, py::arg("nitro") = false, py::arg("drift") = false, py::arg("rescue") = false, py::arg("fire") = false)
        
        .def_readwrite("steer", &PySTKAction::steering_angle, "Steering angle, normalize to -1..1")
        .def_readwrite("acceleration", &PySTKAction::acceleration, "Acceleration, normalize to 0..1")
        .def_readwrite("brake", &PySTKAction::brake, "Hit the brakes. Zero acceleration and brake=True uses reverse gear.")
        .def_readwrite("nitro", &PySTKAction::nitro, "Use nitro")
        .def_readwrite("drift", &PySTKAction::drift, "Drift while turning")
        .def_readwrite("rescue", &PySTKAction::rescue, "Call the rescue bird")
        .def_readwrite("fire", &PySTKAction::fire, "Fire the current pickup item")
        .def("__str__", [](const PySTKAction & a) -> std::string { return ((std::stringstream&)(std::stringstream() << "<Action S:" << a.steering_angle << "  A:" << a.acceleration << "  b:" << (int) a.brake << "  n:" << (int) a.nitro << "  d:" << (int) a.drift << "  r:" << (int) a.rescue << "  f:" << (int) a.fire << " >")).str();});
        add_pickle(cls);
    }
    
    m.def("is_running", &PySTKRace::isRunning,"Is a race running?");
    {
        py::class_<PySTKRace, std::shared_ptr<PySTKRace> >(m, "Race", "The SuperTuxKart race instance")
        .def(py::init<const PySTKRaceConfig &>(),py::arg("config"))
        .def("restart", &PySTKRace::restart,"Restart the current track. Use this function if the race config does not change, instead of creating a new SuperTuxKart object")
        .def("start", &PySTKRace::start,"start the race")
        .def("get_kart_action", &PySTKRace::getKartAction, "Get a kart control state")
        .def("step", (bool (PySTKRace::*)(const std::vector<PySTKAction> &)) &PySTKRace::step, py::arg("action"), "Take a step with an action per agent")
        .def("step", (bool (PySTKRace::*)(const PySTKAction &)) &PySTKRace::step, py::arg("action"), "Take a step with an action for agent 0")
        .def("step", (bool (PySTKRace::*)()) &PySTKRace::step, "Take a step without changing the action")
        .def("stop", &PySTKRace::stop,"Stop the race")
#ifdef SERVER_ONLY
.def_property_readonly("render_data", [](const PySTKRace &) -> py::list {return py::list();}, "rendering data from the last step")
#else
        .def_property_readonly("render_data", &PySTKRace::render_data, "rendering data from the last step")
#endif  // SERVER_ONLY
        .def_property_readonly("config", &PySTKRace::config,"The current race configuration");
    }
    
    m.def("list_tracks", (std::vector<std::string> (*)())&PySTKRace::listTracks, "Return a list of track names (possible values for RaceConfig.track)");
    m.def("list_tracks", (std::vector<std::string> (*)(PySTKRaceConfig::RaceMode))&PySTKRace::listTracks, "Return a list of track names (possible values for RaceConfig.track)");
    m.def("list_karts", &PySTKRace::listKarts, "Return a list of karts to play as (possible values for PlayerConfig.kart");
    
    // Initialize SuperTuxKart
    m.def("init", &path_and_init, py::arg("config"), "Initialize Python SuperTuxKart - this will download the game assets if not already done. Only call this function once per process. Calling it twice will cause a crash.");
    m.def("clean", &PyGlobalEnvironment::cleanup, "Free Python SuperTuxKart, call this once at exit (optional). Will be called atexit otherwise.");
    
    auto atexit = py::module::import("atexit");
        atexit.attr("register")(py::cpp_function([]() {
            // A bit ugly
            PySTKRace::running_kart = nullptr;
            PyGlobalEnvironment::cleanup();
        }));
}

