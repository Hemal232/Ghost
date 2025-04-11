# Ghost / GBSA
Ghost (Ghost Build System / GBSA) is a flexible cross-compiler for Windows and Linux that runs on top of Github Actions for straightforward, unfussy and uninvolved cross-compilation! Here is a complete list of Ghost features:
- [X] C and C++ support.
- [X] Easy integration into already existing projects.
- [X] Simple small and readable XML config.
- [X] Custom OS-dependent auxiliary files for pre-installation of required dependencies or other work before compiling binaries for both Windows and Linux.
- [X] GNU support for Windows.
- [X] GNU support for Linux.
- [ ] Clang support for Windows.
- [X] Clang support for Linux.
- [ ] CMake support for Windows.
- [ ] CMake support for Linux.
- [X] Build process logging.
- [X] Extremely small (<7kb without auxiliary files).

# Installation.
1. Download Ghost ZIP.<br>
2. Unpack `Ghost` directory.<br>
3. Move `Ghost/ghost-build.yml` to `.github/workflows/` directory in your repository.<br>
4. Rename `ghost-build.yml` to `build-release.yml`.<br>
5. Move `ghost-build.py` and `ghost-build.xml` to `ghost-build` directory in your repository.<br><br>
Done!

# Configuration.
This is what the new configuration looks like:
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!-- H17I Github Actions Ghost Build System. -->
<GhostBuild Compiler="NULL" CType="NULL">
    <BuildName>NULL</BuildName>
    <CMainFile>NULL</CMainFile>
    <CFlagsWindows>NULL</CFlagsWindows>
    <CFlagsLinux>NULL</CFlagsLinux>
    <WindowsAuxiliary>NULL</WindowsAuxiliary>
    <LinuxAuxiliary>NULL</LinuxAuxiliary>
</GhostBuild>
```

- <code>GhostBuild::Compiler</code> Attribute (GNU or Clang, case sensitive): The compiler that will be used for compiling the code.
- <code>GhostBuild::CType</code> Attribute (C or C++, case sensitive): Code language, C or C++
- <code>GhostBuild/BuildName</code> Element: Build name, completely optional.
- <code>GhostBuild/CMainFile</code> Element: Relative path to the main executable file.
- <code>GhostBuild/CFlagsWindows</code> Element: Compilation flags for Windows, use `NULL` if no flags needed.
- <code>GhostBuild/CFlagsLinux</code> Element: Compilation flags for Linux, use `NULL` if no flags needed.
- <code>GhostBuild/WindowsAuxiliary</code> Element: Relative path to a pre-compilation executable auxiliary Python file for dependencies installation for Windows, use `NULL` if no aux. files needed.
- <code>GhostBuild/LinuxAuxiliary</code> Element: Relative path to a pre-compilation executable auxiliary Python file for dependencies installation for Linux, use `NULL` if no aux. files needed.

### Notes
Ghost will automatically switch to GNU compiler when compiling to Windows because there is no Clang support for Windows right now.<br
`WindowsAuxiliary` and `LinuxAuxiliary` files must be placed in `ghost-build` directory. When specifying the aux. files you don't need to put `ghost-build/` before the aux. file. The `.py` suffix is also optional, Ghost will find the file without an extension.<br>
Tip: If compiled EXE binary crashes with DLL missing error try appending `--static` to `CFlagsWindows` in your configuration.

# How does it works?
Once Ghost detected a new release:
  - Ghost gets release files.
  - Ghost parses configuration file.
  - Ghost uses Github Actions to run configured compilation process on Windows and Linux.
  - Ghost publishes compiled binaries as an artifacts.

You can check the cross-compilation process on the repository's Github Actions page.<br><hr>

Web version of this documentation: https://h17i.github.io/ghost
