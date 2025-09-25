<div align="center"><img src="nowfocus.svg" width="60"  align="center">  

# *NowFocus* <br> Open-source task timer for linux  

**Avoid multifailing. Master your to-do lists. Track your time.**

</div>
NowFocus is a clean, keyboard-driven project time tracker build with python + GTK that flexibly connects multiple to-do lists with multiple time trackers and displays your current task and time spent in the status bar. 

## Features
- Unlimited flexible combinations of to-do lists and time tracking systems  
- Infinitely nestable lists  
- Inactivity detection that automatically pauses time tracking 
- Pomodoro timer  
- Task prioritization
- Time targets: set a minimum or maximum time for any task or list of tasks and get reminded to follow though 
- Randomness interrupt bell (optional) to keep you on track with tracking your time
- Keyboard-driven interface 
- Offline to-do list cache 
- CLI
- Run a command (or launch an application) when a task is started


<img src="Screenshot-25-09-23-11-42-56.webp" width="500">  
<img src="Screenshot-25-09-23-11-46-14.webp" width="400">  
<img src="Screenshot-25-09-23-11-53-22.webp" width="400">  

<br>

### Currently Supported To-do List Backends

- Simple text or markdown file with indentation based sub-lists
- Any to-do list that supports [CalDav todos](https://en.wikipedia.org/wiki/CalDAV) 
- [todotxt format](http://todotxt.org/)
- [TaskWarrior](https://taskwarrior.org/)
- [Vikunja](https://www.vikunja.io)
- [Photosynthesis Timetracker](https://github.com/Photosynthesis/Timetracker/)  
- [Trello](https://www.trello.com)

### Currently Supported Time Tracker Backends 

- CSV file  
- [ActivityWatch](https://www.activitywatch.net)      
- [Photosynthesis Timetracker](https://github.com/Photosynthesis/Timetracker/)  
- [TimeWarrior](https://timewarrior.net)


## Installation (using pipx) 

1. Run the following in terminal to install with dependencies:
```
sudo apt install pip pipx install gir1.2-appindicator3-0.1 meson libdbus-glib-1-dev patchelf python3.12-venv libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev
pipx ensurepath
pipx install NowFocus
``` 
2. Now run `nowfocus` and check for errors

3. Set up a keybinding (on Ubuntu or Linux Mint), open **Setting > Keyboard > Keyboard Shortcuts > Custom Shortcuts**, set the **command** to `nowfocus`, and pick whatever key combo you'd like.

4. Add the following command to your startup applications: `nowfocus --force` 


## Usage

#### Set up to-do lists and time trackers

Open NowFocus **Settings** from the indicator menu or tasks window and connect your to-do lists and time tracker(s) 

#### Task Window Keybindings

- `F11` Toggle fullscreen
- `Esc` Close task window
- `Enter` Start top task (or make a new task with current search phrase if no results)
- `Ctrl + P` **Pause** current task
- `Ctrl + D` Pause current task and mark it **Done**
- `Ctrl + X` Cancel current task
- `Ctrl + N` **New** task
- `Ctrl + R` **Refresh** todolists
- `Ctrl + L` or `Ctrl + F` **Focus** the task search

#### Commandline Interface

- To raise the task window use simply: `nowfocus`  
- If NowFocus has crashed or failed to shut down nicely use `nowfocus --force`
- To start timing a task: add the task name as the first positional argument. `nowfocus "checking email"`
- To stop timing use `nowfocus stop`
- Start with verbose logging use: `nowfocus -l 3`
- Start with targeted verbose logging use: `nowfocus -s trello`


## Development

### Install from Source

- Install dependencies from above.  
- Clone this repo somewhere (referred to as `YOUR_INSTALL_PATH`)  
- Change to `YOUR_INSTALL_PATH` directory with `cd YOUR_INSTALL_PATH/nowfocus`  
- build python module with `python3 -m build` (this should be done in a venv and will require some dependecies...)  
- pipx install -e --force YOUR_INSTALL_PATH/monotask/  



<!-- 
## Build Flatpak

```
python3 -m build
# python3 flatpak-pip-generator --runtime=org.gnome.Sdk/x86_64/47 PACKAGE # run this for lots of stuff
flatpak run org.flatpak.Builder --force-clean --user --install --install-deps-from=flathub --repo=repo builddir APPID.yaml
flatpak run APPID
```
 -->


<!-- ## Contributing
Package it for your operating system.
Write a connector for your favorite to-do list or time tracker -->
