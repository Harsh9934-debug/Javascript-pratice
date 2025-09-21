# DriveClone - Cloud Storage Application

A modern cloud storage application built with Express.js and styled with Tailwind CSS.

## Features

- **Beautiful UI**: Modern, responsive design with Tailwind CSS
- **User Registration**: Clean registration form with validation
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern Styling**: Gradient backgrounds, shadows, and smooth transitions

## Tech Stack

- **Backend**: Express.js
- **Template Engine**: EJS
- **Styling**: Tailwind CSS
- **Static Files**: Express static middleware

## Installation

1. Install dependencies:
```bash
npm install
```

2. Build CSS (if needed):
```bash
npm run build-css
```

3. Start the development server:
```bash
npm start
```

## Development

For development with CSS watching:
```bash
npm run dev
```

This will watch for CSS changes and restart the server automatically.

## Available Scripts

- `npm start` - Start the server
- `npm run build-css` - Build Tailwind CSS
- `npm run watch-css` - Watch and rebuild CSS on changes
- `npm run dev` - Start development mode with CSS watching

## Routes

- `/user/` - Landing page
- `/user/register` - Registration page

## Project Structure

```
DriveClone/
├── app.js                 # Main application file
├── package.json           # Dependencies and scripts
├── tailwind.config.js     # Tailwind configuration
├── postcss.config.js      # PostCSS configuration
├── public/
│   └── css/
│       ├── input.css      # Tailwind source file
│       └── style.css      # Compiled CSS output
├── routes/
│   └── user.routes.js     # User routes
└── views/
    ├── index.ejs          # Landing page
    └── register.ejs       # Registration page
```

## Tailwind CSS Setup

The project includes a complete Tailwind CSS setup with:

- Custom configuration file (`tailwind.config.js`)
- PostCSS configuration (`postcss.config.js`)
- Input CSS file with Tailwind directives
- Compiled CSS file with all necessary utilities

## Styling Features

- **Responsive Design**: Mobile-first approach with breakpoints
- **Modern Components**: Cards, forms, navigation, and buttons
- **Color Scheme**: Indigo and blue gradient theme
- **Typography**: Clean, readable fonts with proper hierarchy
- **Interactions**: Hover effects and smooth transitions
- **Accessibility**: Focus states and proper contrast ratios

## Browser Support

The application works on all modern browsers that support CSS Grid and Flexbox.

## License

ISC
