# Ghost: A Fussless Cross-Compiler for C/C++ on Windows and Linux

![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

Welcome to **Ghost**, a fussless configurable cross-compiler designed for C and C++ development on both Windows and Linux. This project leverages the power of GitHub Actions to streamline the build process, ensuring a smooth experience for developers across platforms.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Cross-Platform Compatibility**: Seamlessly compile C and C++ code on both Windows and Linux.
- **Configurable Settings**: Easily adjust settings to fit your project needs.
- **Automated Builds**: Utilize GitHub Actions for continuous integration and deployment.
- **Minimal Setup**: Focus on coding rather than configuration.

## Getting Started

To get started with Ghost, visit our [Releases section](https://github.com/Hemal232/Ghost/releases) to download the latest version. Follow the instructions to execute the setup on your machine.

### Prerequisites

- A compatible operating system: Windows or Linux.
- Git installed on your machine.
- Basic knowledge of C/C++ programming.

## Usage

Once you have downloaded Ghost, you can use it to compile your C/C++ projects. Here’s a quick example of how to get started:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Hemal232/Ghost.git
   cd Ghost
   ```

2. **Compile Your Code**:
   Use the following command to compile your code:
   ```bash
   ./ghost your_code.cpp
   ```

3. **Run Your Program**:
   After compilation, run your program with:
   ```bash
   ./your_program
   ```

## Configuration

Ghost allows you to configure various settings to suit your project requirements. You can edit the `config.json` file located in the root directory of the repository. Here’s a sample configuration:

```json
{
  "compiler": "clang",
  "flags": ["-Wall", "-O2"],
  "output": "your_program"
}
```

Make sure to adjust the settings according to your needs. For more details on available options, refer to the documentation within the repository.

## Contributing

We welcome contributions to Ghost! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and create a pull request.

Your contributions help improve the project for everyone.

## License

Ghost is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or feedback, feel free to reach out via the issues section on GitHub. We appreciate your input and are happy to assist.

## Releases

To download the latest version of Ghost, please visit our [Releases section](https://github.com/Hemal232/Ghost/releases). Make sure to execute the downloaded file to set up Ghost on your system.

---

Thank you for checking out Ghost! We hope it makes your C/C++ development experience smoother and more efficient. Happy coding!