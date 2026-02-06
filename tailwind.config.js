module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/*.html",
    "./**/*.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        "custom-light": {
          "primary": "#0ea5e9",
          "primary-content": "#ffffff",

          "secondary": "#14b8a6",
          "secondary-content": "#ffffff",

          "accent": "#f59e0b",
          "accent-content": "#ffffff",

          "neutral": "#1f2937",
          "neutral-content": "#f3f4f6",

          "base-100": "#ffffff",
          "base-200": "#f3f4f6",
          "base-300": "#e5e7eb",

          "info": "#0ea5e9",
          "success": "#10b981",
          "warning": "#f59e0b",
          "error": "#ef4444",
        },
      },
      {
        "custom-dark": {
          "primary": "#0ea5e9",
          "primary-content": "#ffffff",

          "secondary": "#14b8a6",
          "secondary-content": "#ffffff",

          "accent": "#f59e0b",
          "accent-content": "#ffffff",

          "neutral": "#e5e7eb",
          "neutral-content": "#1f2937",

          "base-100": "#111827",
          "base-200": "#0f172a",
          "base-300": "#020617",

          "info": "#38bdf8",
          "success": "#34d399",
          "warning": "#fbbf24",
          "error": "#f87171",
        },
      },
    ],
  },
}
