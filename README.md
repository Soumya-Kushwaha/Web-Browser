# Personal Web Browser 🌐

A lightweight, feature-rich web browser built with Python and PyQt5. This desktop application provides a clean interface with essential browsing functionalities.

## ✨ Features

- Clean and intuitive user interface
- Navigation toolbar with common browser actions
- URL bar with real-time updates
- Maximized window display for optimal viewing
- Home page functionality (Google.com)
- Forward and backward navigation
- Page reload capability

## 🔧 Prerequisites

Before running this application, make sure you have the following installed:

```bash
- Python 3.x
- PyQt5
- PyQtWebEngine
```

## 📦 Installation

1. Install the required packages:

```bash
pip install PyQt5 PyQtWebEngine
```

2. Clone this repository:

```bash
git clone https://github.com/yourusername/personal-web-browser.git
cd personal-web-browser
```

3. Run the application:

```bash
python browser.py
```

## 🛠️ Technical Details

### Components Used

- **QMainWindow**: Main application window controller
- **QWebEngineView**: Web page rendering engine
- **QToolBar**: Navigation bar container
- **QAction**: Button actions for navigation
- **QLineEdit**: URL input field

### Key Features Implementation

- **Navigation Controls**: Back, Forward, Reload, and Home buttons
- **URL Management**: Real-time URL updates and manual URL entry
- **Window Management**: Maximized window display for better user experience
- **Event Handling**: Connected signals and slots for user interactions

## 🌟 Usage

1. Launch the application
2. Use the navigation toolbar to browse:
   - Click 'Back' to return to the previous page
   - Click 'Forward' to go to the next page
   - Click 'Reload' to refresh the current page
   - Click 'Home' to return to Google.com
3. Enter URLs directly in the URL bar and press Enter to navigate

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- PyQt5 team for the excellent framework
- Qt Company for the QtWebEngine component
- Google for providing the default homepage

## 📞 Contact

For any queries or suggestions, please open an issue in the GitHub repository.

---
Made with ❤️ using Python and PyQt5
