/**
 * Looking-Glass Theme & Structural Clarity - Tailwind CSS Preset
 * Utility over ornament. Carroll's wit in structure, naming and typography.
 */

module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          slate: '#0F172A',            // Looking-Glass Slate (Canvas)
          boardSlate: '#1B2540',       // Board Slate (Checkerboard square alt)
          teal: '#2DD4BF',             // Cheshire Teal (Accent / action: 9.59:1 AAA)
          gold: '#F59E0B',             // White Rabbit Gold (Warm accent / nexus: 8.31:1 AAA)
          amber: '#F59E0B',            // Legacy alias
          redQueen: '#FDA4AF',         // Red Queen (Caution / threshold: 9.44:1 AAA)
          vellum: '#F5EFE0',           // Vellum (Body type: 15.56:1 AAA)
          chalk: '#F5EFE0',            // Legacy alias
          brass: '#B08D3C',            // Brass Hairline (Decorative rules only: 5.71:1)
        },
        surface: {
          canvas: '#0F172A',
          board: '#1B2540',
          card: '#141D30',
          subtle: '#1B2540',
        },
        border: {
          brass: '#B08D3C',
          doubleBrass: '#B08D3C',
          teal: '#2DD4BF',
          gold: '#F59E0B',
          redQueen: '#FDA4AF',
        },
      },
      fontFamily: {
        display: ['EB Garamond', 'Cormorant Garamond', 'Garamond', 'Georgia', 'Times New Roman', 'serif'],
        body: ['Space Grotesk', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        technical: ['JetBrains Mono', 'Fira Code', 'ui-monospace', 'monospace'],
      },
      letterSpacing: {
        technical: '0.05em',
        wide: '0.08em',
      },
      borderRadius: {
        xs: '2px',
        sm: '4px',
        md: '6px',
      },
      boxShadow: {
        technical: '0 1px 3px 0 rgba(15, 23, 42, 0.08)',
        tealGlow: '0 0 15px rgba(45, 212, 191, 0.25)',
        goldGlow: '0 0 15px rgba(245, 158, 11, 0.25)',
      },
    },
  },
};
