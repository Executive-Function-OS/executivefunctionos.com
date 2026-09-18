/**
 * Structural Clarity & Dynamic Resonance - Tailwind CSS Preset
 * Extracted from Canva AI Visual Identity System
 */

module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          slate: '#0F172A',      // Primary Base / Deep Slate
          teal: '#0D9488',       // Accent / Action / Signal Teal
          amber: '#D97706',      // Warm Accent / Resonant Amber
          chalk: '#F8FAFC',      // Neutral Canvas / Chalk White
        },
        surface: {
          light: '#FFFFFF',
          dark: '#1E293B',
          subtleLight: '#F1F5F9',
          subtleDark: '#162032',
        },
        border: {
          hairline: '#E2E8F0',
          darkHairline: '#334155',
          teal: '#0D9488',
          amber: '#D97706',
        },
      },
      fontFamily: {
        display: ['Space Grotesk', 'Inter', 'sans-serif'],
        technical: ['JetBrains Mono', 'Fira Code', 'monospace'],
        editorial: ['Charter', 'Inter', 'serif'],
      },
      letterSpacing: {
        technical: '0.05em',
        wide: '0.1em',
      },
      borderRadius: {
        xs: '2px',
        sm: '4px',
        md: '6px',
      },
      boxShadow: {
        technical: '0 1px 3px 0 rgba(15, 23, 42, 0.08), 0 1px 2px -1px rgba(15, 23, 42, 0.08)',
        tealGlow: '0 0 15px rgba(13, 148, 136, 0.25)',
        amberGlow: '0 0 15px rgba(217, 119, 6, 0.25)',
      },
    },
  },
};
