import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// En développement, les appels /api sont redirigés vers le backend Django.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: { "/api": "http://127.0.0.1:8000" },
  },
});
