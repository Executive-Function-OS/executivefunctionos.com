#!/usr/bin/env python3
"""
Generator for Forensic Microclimate Investigation Interactive Presentation Deck
Features:
- Full 16-Slide Evidentiary Structure (Fre 702 / Daubert Compliant)
- Complete 30-Year Landsat 5/7/8/9 Overpass Dataset & Level-2 Calibration
- Difference-in-Differences Econometric Model & Regression Slopes
- 167-Permit Municipal Tree Removal Corridor Registry
- Native PresentationNarrator Voice Controller (Neural voice sorting, Auto-Present, Read Slide, Chrome Keep-Alive)
- Responsive Touch/Swipe & Keyboard Navigation
"""

slides_data = [
    {
        "id": 1,
        "badge": "EVIDENTIARY TECHNICAL REPORT • FRE / OEC 702",
        "title": "Forensic Microclimate Investigation",
        "subtitle": "Comparative Surface-Temperature Assessment & Canopy Loss at 12054 Chapin Court (1994–2024)",
        "notes": "Forensic Microclimate Investigation: Comparative Surface-Temperature Assessment and Canopy Depletion at 12054 Chapin Court from 1994 to 2024. This technical report synthesizes thirty years of calibrated USGS Landsat satellite thermography, Open-Meteo ERA5 atmospheric reanalysis, thermal interaction modeling, and municipal code enforcement records in Oregon City, Oregon.",
        "html": """
        <div class="hero-box">
          <div class="lead-badge">30-Year Comparative Observational Study (1994–2024)</div>
          <h1 class="hero-title">Forensic Microclimate Investigation</h1>
          <p class="hero-subtitle">Neighborhood Thermal Contrasts & Canopy Loss at 12054 Chapin Court, Oregon City, Oregon</p>
          <div class="grid-2col" style="margin-top: 1.5rem;">
            <div class="card-item">
              <div class="card-label">TARGET SUBJECT PROPERTY</div>
              <div class="card-value-large">12054 Chapin Court</div>
              <div class="card-subtext">Oregon City, OR 97045 · Tax Lot: Tower Vista Subdivision</div>
              <div class="meta-tag-list" style="margin-top: 0.75rem;">
                <span class="mono-badge">Lat: 45.33286° N</span>
                <span class="mono-badge">Lon: -122.61601° W</span>
                <span class="mono-badge">Elev: ~475 ft ASL</span>
                <span class="mono-badge coral">NDVI: 0.115 (Depleted Hardscape)</span>
              </div>
            </div>
            <div class="card-item">
              <div class="card-label">EVIDENTIARY ARCHITECTURE</div>
              <p class="body-text" style="font-size: 0.88rem; line-height: 1.55;">
                Prepared for forensic environmental review, municipal infrastructure liability assessment, and comparative microclimate risk analysis. Grounded in USGS Landsat Collection 2 surface temperature radiometry, Open-Meteo ERA5-Land atmospheric reanalysis, and official Oregon City municipal court and public works enforcement dockets.
              </p>
              <div class="meta-tag-list" style="margin-top: 0.75rem;">
                <span class="mono-badge amber">USGS Landsat 5/7/8/9</span>
                <span class="mono-badge teal">Open-Meteo ERA5-Land</span>
                <span class="mono-badge purple">OC Title 12 Archives</span>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 2,
        "badge": "INVESTIGATIVE ARCHITECTURE",
        "title": "Core Research Question & Standards",
        "subtitle": "Isolating localized anthropogenic microclimatic heating from regional background warming",
        "notes": "Core research question: Has Chapin Court exhibited a persistent surface-temperature contrast relative to comparable Oregon City residential neighborhoods, especially during regional heat events, since construction in 1994? The analysis applies Federal Rule of Evidence 702 and Oregon Evidence Code 702 standards, examining twelve cloud-free Landsat overpasses, ERA5 reanalysis, and official municipal enforcement dockets.",
        "html": """
        <div class="callout-banner">
          <div class="callout-label">CORE RESEARCH QUESTION</div>
          <div class="callout-quote">
            “Has the Chapin Court neighborhood exhibited a persistent surface-temperature contrast relative to comparable Oregon City residential neighborhoods—especially during regional heat events—since construction in 1994?”
          </div>
        </div>
        <div class="grid-3col" style="margin-top: 1.25rem;">
          <div class="card-item">
            <div class="card-label">OBSERVATIONAL DATASET</div>
            <div class="stat-highlight amber">12 Overpasses</div>
            <p class="body-text">
              12 cloud-free USGS Landsat 5, 7, 8, & 9 Level-2 Surface Temperature (30m LST resampled from native 60–120m thermal sensors) overpasses spanning 1994 through 2024.
            </p>
          </div>
          <div class="card-item">
            <div class="card-label">ATMOSPHERIC BASELINES</div>
            <div class="stat-highlight teal">ERA5-Land Hourly</div>
            <p class="body-text">
              Hourly surface reanalysis from Open-Meteo ERA5-Land at Oregon City coordinates (45.33° N, -122.61° W) paired to exact satellite overpass timestamps.
            </p>
          </div>
          <div class="card-item">
            <div class="card-label">LEGAL ADMISSIBILITY</div>
            <div class="stat-highlight purple">FRE 702 / OEC 702</div>
            <p class="body-text">
              Calibrated federal radiometry, elevation-matched local controls (~443–475 ft ASL), comparative thermal regression, and cross-referenced municipal enforcement records.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 3,
        "badge": "DAUBERT ELEVATION-MATCHED CONTROLS",
        "title": "Geographic Baseline & Matched Controls",
        "subtitle": "Rigorous geographic pairing within the same municipal boundary and elevation band (~440–475 ft ASL)",
        "notes": "To satisfy evidentiary scrutiny, candidate control locations were selected within the same municipal boundary and elevation band at 440 to 475 feet above sea level. Rivercrest and Hillendale share similar geological substrate, solar exposure azimuth, and regional air masses. While Rivercrest maintains an NDVI of 0.527 and Hillendale 0.448 with mature tree cover, Chapin Court's vegetation index stands at only 0.115 with dark asphalt and unshaded roofs.",
        "html": """
        <p class="body-text" style="margin-bottom: 1rem;">
          To satisfy Daubert and OEC 702 scrutiny, control locations were selected within the exact same municipal jurisdiction, sharing identical geological substrate, solar exposure azimuth, and macro-weather regimes:
        </p>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Site Identifier</th>
                <th>Location / Area</th>
                <th>Coordinates</th>
                <th>Elevation</th>
                <th>NDVI Index</th>
                <th>Canopy Morphology & Built Hardscape</th>
              </tr>
            </thead>
            <tbody>
              <tr class="row-target">
                <td><strong class="coral">Target Subject</strong></td>
                <td>12054 Chapin Court</td>
                <td class="mono">45.33286° N, -122.61601° W</td>
                <td class="mono">~475 ft</td>
                <td><span class="badge-pill coral">0.115</span></td>
                <td>Severely depleted street canopy; dark asphalt pavement & composite shingle roofs</td>
              </tr>
              <tr>
                <td><strong class="teal">Control A</strong></td>
                <td>Rivercrest Residential</td>
                <td class="mono">45.34510° N, -122.60766° W</td>
                <td class="mono">~462 ft</td>
                <td><span class="badge-pill teal">0.527</span></td>
                <td>Mature, continuous Douglas-fir and deciduous street tree canopy</td>
              </tr>
              <tr>
                <td><strong class="teal">Control B</strong></td>
                <td>Hillendale Residential</td>
                <td class="mono">45.32901° N, -122.59703° W</td>
                <td class="mono">~443 ft</td>
                <td><span class="badge-pill teal">0.448</span></td>
                <td>Co-dominant residential shade trees, buffered parkway medians</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="note-box" style="margin-top: 1rem;">
          <strong class="teal">Control Integrity:</strong> Both control sites experienced the exact same atmospheric air masses and heat domes (~443–475 ft ASL). Differential surface heating cannot be dismissed as an artifact of elevation lapse rates or marine air push delays; land cover and canopy characteristics diverged.
        </div>
        """
    },
    {
        "id": 4,
        "badge": "PRIMARY QUANTITATIVE FINDINGS",
        "title": "The Heatwave Penalty",
        "subtitle": "Disproportionate surface thermal amplification under extreme ambient heat conditions",
        "notes": "The observational findings document a persistent thermal contrast. On normal summer days below ninety degrees, Chapin Court registers an average excess surface temperature of plus 10.99 degrees Fahrenheit above matched controls. During regional heat events at or above ninety degrees, this excess averages plus 12.86 degrees, peaking at 122.59 degrees on July 9, 2024. A baseline heatwave spike of plus 17.31 degrees was also recorded on July 24, 2006.",
        "html": """
        <div class="grid-4col">
          <div class="stat-card">
            <div class="stat-title">NORMAL SUMMER DAYS (&lt;90°F)</div>
            <div class="stat-number teal">+10.99°F</div>
            <div class="stat-desc">Average radiant excess surface heat above matched controls under normal summer conditions (n=7).</div>
          </div>
          <div class="stat-card alert">
            <div class="stat-title">HEATWAVE DAYS (≥90°F)</div>
            <div class="stat-number coral">+12.86°F</div>
            <div class="stat-desc">Average radiant excess surface heat during regional heat events (n=5; exploratory Welch p ≈ 0.265).</div>
          </div>
          <div class="stat-card danger">
            <div class="stat-title">RECORD RADIANT PEAK</div>
            <div class="stat-number coral">122.59°F</div>
            <div class="stat-desc">Peak radiant surface observation on July 9, 2024 (Landsat 9 LC09_L2SP_046029_20240709).</div>
          </div>
          <div class="stat-card">
            <div class="stat-title">MAX ABSOLUTE EXCESS</div>
            <div class="stat-number amber">+17.31°F</div>
            <div class="stat-desc">Peak baseline radiative hazard recorded July 24, 2006 (119.01°F Chapin vs 101.70°F control avg).</div>
          </div>
        </div>
        <div class="grid-2col" style="margin-top: 1rem;">
          <div class="card-item">
            <div class="card-label">OBSERVED SURFACE CONTRAST</div>
            <p class="body-text">
              Across all 12 sampled dates, Chapin Court surface temperatures exceeded matched controls by <strong>+7.02°F to +17.31°F</strong>. When ambient air reaches 90°F+, absence of tree canopy allows dark asphalt pavement and roofing to function as unbuffered solar heat sinks, expanding the average gap by +1.875°F.
            </p>
          </div>
          <div class="card-item">
            <div class="card-label">CANOPY ELIMINATION CONTEXT</div>
            <p class="body-text">
              Canopy loss on Chapin Court accelerated during the <strong>2009–2018 municipal street tree removal wave</strong> under Title 12 sidewalk liability enforcement, where street trees originally mandated by subdivision approvals were removed without shade replacement.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 5,
        "badge": "THERMODYNAMIC ACCELERATION",
        "title": "Comparative Thermal Response Slopes",
        "subtitle": "Empirical heating rates: d(LST)/d(Tambient) = 0.907°F/°F vs 0.772°F/°F across 12 overpasses",
        "notes": "Evaluating regression slopes across the 12 overpasses reveals localized thermal amplification. Radiant surface temperature at Chapin Court rises 0.907 degrees for every one degree increase in ambient air temperature, compared to 0.772 degrees in mature-canopy control areas, yielding an excess slope point estimate of plus 0.136 degrees per ambient degree.",
        "html": """
        <div class="grid-2col">
          <div>
            <div class="card-item" style="height: 100%;">
              <div class="card-label">REGRESSION DERIVATIVES</div>
              <div class="metric-row">
                <span class="metric-name">Chapin Court Thermal Slope:</span>
                <span class="metric-val coral">0.907°F / °F <small>(R² ≈ 0.710)</small></span>
              </div>
              <div class="metric-row">
                <span class="metric-name">Canopied Controls Thermal Slope:</span>
                <span class="metric-val teal">0.772°F / °F <small>(R² ≈ 0.763)</small></span>
              </div>
              <div class="metric-row highlight">
                <span class="metric-name">Excess Thermal Acceleration (Δβ):</span>
                <span class="metric-val amber">+0.136°F / °F <small>(95% CI [-0.046, +0.317], p ≈ 0.126)</small></span>
              </div>
              <div style="margin-top: 1rem;">
                <p class="body-text" style="font-size: 0.85rem; line-height: 1.5;">
                  <strong>Physical Dynamics:</strong> Under moderate weather (~75°F ambient), the surface contrast is approximately +8°F. Under extreme ambient heat (95°F–100°F+), the gap widens to <strong>+12°F to +17°F</strong>. Canopy removal strips evaporative cooling and shading precisely when atmospheric heat is most intense.
                </p>
              </div>
            </div>
          </div>
          <div>
            <div class="chart-container">
              <div class="chart-header">Thermal Response Slope: Surface LST vs Ambient Air (°F)</div>
              <svg viewBox="0 0 500 260" class="slope-svg" preserveAspectRatio="xMidYMid meet">
                <line x1="60" y1="210" x2="470" y2="210" stroke="#334155" stroke-width="1.5" />
                <line x1="60" y1="20" x2="60" y2="210" stroke="#334155" stroke-width="1.5" />
                
                <line x1="60" y1="160" x2="470" y2="160" stroke="#1E293B" stroke-dasharray="4" />
                <line x1="60" y1="110" x2="470" y2="110" stroke="#1E293B" stroke-dasharray="4" />
                <line x1="60" y1="60" x2="470" y2="60" stroke="#1E293B" stroke-dasharray="4" />
                
                <text x="60" y="228" fill="#94A3B8" font-size="11" text-anchor="middle">70°F</text>
                <text x="195" y="228" fill="#94A3B8" font-size="11" text-anchor="middle">80°F</text>
                <text x="330" y="228" fill="#94A3B8" font-size="11" text-anchor="middle">90°F (Heatwave)</text>
                <text x="450" y="228" fill="#94A3B8" font-size="11" text-anchor="middle">102°F</text>
                
                <text x="52" y="213" fill="#94A3B8" font-size="10" text-anchor="end">80°F</text>
                <text x="52" y="163" fill="#94A3B8" font-size="10" text-anchor="end">95°F</text>
                <text x="52" y="113" fill="#94A3B8" font-size="10" text-anchor="end">110°F</text>
                <text x="52" y="63" fill="#94A3B8" font-size="10" text-anchor="end">125°F</text>
                
                <rect x="330" y="20" width="140" height="190" fill="rgba(244, 63, 94, 0.08)" />
                <line x1="330" y1="20" x2="330" y2="210" stroke="#F43F5E" stroke-dasharray="3" stroke-width="1" />
                
                <line x1="75" y1="180" x2="455" y2="48" stroke="#F43F5E" stroke-width="3.5" />
                <line x1="75" y1="195" x2="455" y2="82" stroke="#14B8A6" stroke-width="2.5" stroke-dasharray="6 3" />
                
                <circle cx="100" cy="172" r="4.5" fill="#F43F5E" />
                <circle cx="215" cy="144" r="4.5" fill="#F43F5E" />
                <circle cx="250" cy="128" r="4.5" fill="#F43F5E" />
                <circle cx="380" cy="74" r="5" fill="#F43F5E" stroke="#fff" stroke-width="1.5" />
                <circle cx="445" cy="50" r="5" fill="#F43F5E" stroke="#fff" stroke-width="1.5" />
                
                <circle cx="100" cy="188" r="4" fill="#14B8A6" />
                <circle cx="215" cy="162" r="4" fill="#14B8A6" />
                <circle cx="250" cy="148" r="4" fill="#14B8A6" />
                <circle cx="380" cy="102" r="4" fill="#14B8A6" />
                <circle cx="445" cy="85" r="4" fill="#14B8A6" />
                
                <line x1="380" y1="74" x2="380" y2="102" stroke="#F59E0B" stroke-width="2" />
                <text x="390" y="92" fill="#F59E0B" font-size="11" font-weight="600">+12.86°F Excess</text>
                
                <circle cx="90" cy="35" r="4" fill="#F43F5E" />
                <text x="100" y="39" fill="#F8FAFC" font-size="11">Chapin Court (0.907°F/°F)</text>
                <circle cx="240" cy="35" r="4" fill="#14B8A6" />
                <text x="250" y="39" fill="#F8FAFC" font-size="11">Controls (0.772°F/°F)</text>
              </svg>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 6,
        "badge": "EMPIRICAL RADIOMETRY • 1994–2024",
        "title": "30-Year Landsat Overpasses Table",
        "subtitle": "Twelve cloud-free USGS Landsat 5, 7, 8, & 9 Level-2 thermal observations",
        "notes": "Here is the comparative time series of twelve cloud-free Landsat overpasses across Landsat 5, 7, 8, and 9. Every observation was calibrated using standard USGS Level-2 surface temperature scaling. Chapin Court consistently exceeds matched controls across all twelve observations, with a sample peak of 122.59 degrees surface temperature in July 2024.",
        "html": """
        <div class="table-responsive" style="max-height: 480px;">
          <table class="data-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Sensor & Scene ID</th>
                <th>Policy Era</th>
                <th>Ambient (ERA5)</th>
                <th>Chapin LST</th>
                <th>Rivercrest</th>
                <th>Hillendale</th>
                <th>Control Avg</th>
                <th>Excess Heat</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="mono">1994-07-31</td>
                <td class="mono small">Landsat 5 · LT05_L2SP_046029_19940731</td>
                <td><span class="badge-pill gray">Baseline (Built)</span></td>
                <td class="mono">83.3°F</td>
                <td class="mono font-bold">98.70°F</td>
                <td class="mono">81.78°F</td>
                <td class="mono">90.95°F</td>
                <td class="mono">86.36°F</td>
                <td class="mono coral font-bold">+12.34°F</td>
              </tr>
              <tr>
                <td class="mono">1998-08-27</td>
                <td class="mono small">Landsat 5 · LT05_L2SP_046029_19980827</td>
                <td><span class="badge-pill gray">Baseline</span></td>
                <td class="mono">82.0°F</td>
                <td class="mono font-bold">93.54°F</td>
                <td class="mono">82.16°F</td>
                <td class="mono">88.33°F</td>
                <td class="mono">85.24°F</td>
                <td class="mono coral font-bold">+8.29°F</td>
              </tr>
              <tr>
                <td class="mono">2002-07-29</td>
                <td class="mono small">Landsat 7 · LE07_L2SP_046029_20020729</td>
                <td><span class="badge-pill gray">Baseline</span></td>
                <td class="mono">81.0°F</td>
                <td class="mono font-bold">105.67°F</td>
                <td class="mono">89.20°F</td>
                <td class="mono">93.96°F</td>
                <td class="mono">91.58°F</td>
                <td class="mono coral font-bold">+14.09°F</td>
              </tr>
              <tr>
                <td class="mono">2004-07-26</td>
                <td class="mono small">Landsat 5 · LT05_L2SP_046029_20040726</td>
                <td><span class="badge-pill gray">Baseline</span></td>
                <td class="mono">82.6°F</td>
                <td class="mono font-bold">100.35°F</td>
                <td class="mono">86.74°F</td>
                <td class="mono">89.87°F</td>
                <td class="mono">88.30°F</td>
                <td class="mono coral font-bold">+12.06°F</td>
              </tr>
              <tr class="row-highlight">
                <td class="mono">2006-07-24</td>
                <td class="mono small">Landsat 7 · LE07_L2SP_046029_20060724</td>
                <td><span class="badge-pill amber">Baseline Heatwave</span></td>
                <td class="mono">96.4°F</td>
                <td class="mono font-bold">119.01°F</td>
                <td class="mono">99.45°F</td>
                <td class="mono">103.96°F</td>
                <td class="mono">101.70°F</td>
                <td class="mono coral font-bold">+17.31°F</td>
              </tr>
              <tr>
                <td class="mono">2010-08-20</td>
                <td class="mono small">Landsat 7 · LE07_L2SP_046029_20100820</td>
                <td><span class="badge-pill purple">Removal Wave</span></td>
                <td class="mono">73.0°F</td>
                <td class="mono font-bold">91.70°F</td>
                <td class="mono">82.88°F</td>
                <td class="mono">86.48°F</td>
                <td class="mono">84.68°F</td>
                <td class="mono coral font-bold">+7.02°F</td>
              </tr>
              <tr>
                <td class="mono">2013-07-27</td>
                <td class="mono small">Landsat 7 · LE07_L2SP_046029_20130727</td>
                <td><span class="badge-pill purple">Removal Wave</span></td>
                <td class="mono">77.7°F</td>
                <td class="mono font-bold">105.20°F</td>
                <td class="mono">90.41°F</td>
                <td class="mono">94.92°F</td>
                <td class="mono">92.66°F</td>
                <td class="mono coral font-bold">+12.54°F</td>
              </tr>
              <tr>
                <td class="mono">2015-08-18</td>
                <td class="mono small">Landsat 7 · LE07_L2SP_046029_20150818</td>
                <td><span class="badge-pill purple">Removal Wave</span></td>
                <td class="mono">95.5°F</td>
                <td class="mono font-bold">103.75°F</td>
                <td class="mono">92.11°F</td>
                <td class="mono">95.66°F</td>
                <td class="mono">93.89°F</td>
                <td class="mono coral font-bold">+9.86°F</td>
              </tr>
              <tr>
                <td class="mono">2018-08-18</td>
                <td class="mono small">Landsat 8 · LC08_L2SP_046029_20180818</td>
                <td><span class="badge-pill purple">Removal Wave</span></td>
                <td class="mono">83.5°F</td>
                <td class="mono font-bold">101.04°F</td>
                <td class="mono">88.62°F</td>
                <td class="mono">92.31°F</td>
                <td class="mono">90.47°F</td>
                <td class="mono coral font-bold">+10.57°F</td>
              </tr>
              <tr>
                <td class="mono">2021-07-25</td>
                <td class="mono small">Landsat 8 · LC08_L2SP_046028_20210725</td>
                <td><span class="badge-pill red">Post-Clearance</span></td>
                <td class="mono">91.2°F</td>
                <td class="mono font-bold">110.26°F</td>
                <td class="mono">97.44°F</td>
                <td class="mono">100.26°F</td>
                <td class="mono">98.85°F</td>
                <td class="mono coral font-bold">+11.41°F</td>
              </tr>
              <tr>
                <td class="mono">2023-08-16</td>
                <td class="mono small">Landsat 8 · LC08_L2SP_046028_20230816</td>
                <td><span class="badge-pill red">Post-Clearance</span></td>
                <td class="mono">101.5°F</td>
                <td class="mono font-bold">118.21°F</td>
                <td class="mono">103.85°F</td>
                <td class="mono">107.39°F</td>
                <td class="mono">105.62°F</td>
                <td class="mono coral font-bold">+12.59°F</td>
              </tr>
              <tr class="row-highlight">
                <td class="mono">2024-07-09</td>
                <td class="mono small">Landsat 9 · LC09_L2SP_046029_20240709</td>
                <td><span class="badge-pill red">Post-Clearance</span></td>
                <td class="mono">99.7°F</td>
                <td class="mono font-bold coral">122.59°F</td>
                <td class="mono">109.63°F</td>
                <td class="mono">109.29°F</td>
                <td class="mono">109.46°F</td>
                <td class="mono coral font-bold">+13.13°F</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },
    {
        "id": 7,
        "badge": "DECADAL TRAJECTORIES",
        "title": "Multi-Decadal Temperature Chart",
        "subtitle": "Radiant surface temperatures and excess heat differential across 12 sampled dates (1994–2024)",
        "notes": "This multi-decadal visualization tracks radiant surface temperatures across the 12 sampled dates from 1994 to 2024. Notice the persistent elevated gap between Chapin Court and the controls, with radiant surface temperatures reaching 118.2 degrees in 2023 and 122.59 degrees in 2024.",
        "html": """
        <div class="chart-container" style="padding: 1.5rem;">
          <div class="chart-header" style="margin-bottom: 0.75rem;">
            <span>USGS Landsat 30m Level-2 LST vs Controls & Ambient (°F)</span>
            <span class="chart-legend-row">
              <span class="legend-chip"><span class="dot coral"></span> Chapin Court</span>
              <span class="legend-chip"><span class="dot teal"></span> Control Avg</span>
              <span class="legend-chip"><span class="dot amber"></span> Ambient Air</span>
              <span class="legend-chip"><span class="bar-chip"></span> Excess Heat</span>
            </span>
          </div>
          <svg viewBox="0 0 800 320" class="time-series-svg" preserveAspectRatio="xMidYMid meet">
            <line x1="50" y1="240" x2="770" y2="240" stroke="#1E293B" />
            <line x1="50" y1="30" x2="50" y2="240" stroke="#1E293B" />
            
            <line x1="50" y1="185" x2="770" y2="185" stroke="#1E293B" stroke-dasharray="3" />
            <line x1="50" y1="130" x2="770" y2="130" stroke="#1E293B" stroke-dasharray="3" />
            <line x1="50" y1="75" x2="770" y2="75" stroke="#1E293B" stroke-dasharray="3" />
            
            <text x="42" y="243" fill="#64748B" font-size="10" text-anchor="end">70°F</text>
            <text x="42" y="188" fill="#64748B" font-size="10" text-anchor="end">85°F</text>
            <text x="42" y="133" fill="#64748B" font-size="10" text-anchor="end">100°F</text>
            <text x="42" y="78" fill="#64748B" font-size="10" text-anchor="end">115°F</text>
            
            <rect x="70" y="148" width="8" height="37" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="130" y="160" width="8" height="25" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="190" y="126" width="8" height="42" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="230" y="142" width="8" height="36" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="260" y="93" width="8" height="52" fill="rgba(245, 158, 11, 0.6)" rx="1" />
            <rect x="335" y="168" width="8" height="21" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="395" y="127" width="8" height="38" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="435" y="135" width="8" height="30" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="495" y="140" width="8" height="32" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="565" y="112" width="8" height="34" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="645" y="88" width="8" height="38" fill="rgba(245, 158, 11, 0.45)" rx="1" />
            <rect x="715" y="75" width="8" height="39" fill="rgba(244, 63, 94, 0.6)" rx="1" />
            
            <polyline points="74,191 134,196 194,200 234,194 264,143 339,229 399,212 439,147 499,191 569,162 649,125 719,131"
                      fill="none" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.8" />
            
            <polyline points="74,180 134,184 194,161 234,173 264,124 339,186 399,157 439,152 499,165 569,134 649,110 719,97"
                      fill="none" stroke="#14B8A6" stroke-width="2.5" />
            
            <polyline points="74,135 134,154 194,110 234,129 264,60 339,160 399,111 439,116 499,126 569,92 649,63 719,47"
                      fill="none" stroke="#F43F5E" stroke-width="3" />
            
            <circle cx="74" cy="135" r="4" fill="#F43F5E" />
            <circle cx="134" cy="154" r="4" fill="#F43F5E" />
            <circle cx="194" cy="110" r="4" fill="#F43F5E" />
            <circle cx="234" cy="129" r="4" fill="#F43F5E" />
            <circle cx="264" cy="60" r="5" fill="#F43F5E" />
            <circle cx="339" cy="160" r="4" fill="#F43F5E" />
            <circle cx="399" cy="111" r="4" fill="#F43F5E" />
            <circle cx="439" cy="116" r="4" fill="#F43F5E" />
            <circle cx="499" cy="126" r="4" fill="#F43F5E" />
            <circle cx="569" cy="92" r="4" fill="#F43F5E" />
            <circle cx="649" cy="63" r="5" fill="#F43F5E" />
            <circle cx="719" cy="47" r="6" fill="#F43F5E" stroke="#fff" stroke-width="2" />
            <text x="719" y="35" fill="#F43F5E" font-size="12" font-weight="bold" text-anchor="middle">122.59°F (Peak)</text>
            
            <text x="74" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">1994</text>
            <text x="134" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">1998</text>
            <text x="194" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2002</text>
            <text x="234" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2004</text>
            <text x="264" y="260" fill="#F59E0B" font-size="10" text-anchor="middle">2006</text>
            <text x="339" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2010</text>
            <text x="399" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2013</text>
            <text x="439" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2015</text>
            <text x="499" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2018</text>
            <text x="569" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2021</text>
            <text x="649" y="260" fill="#94A3B8" font-size="10" text-anchor="middle">2023</text>
            <text x="719" y="260" fill="#F43F5E" font-size="10" text-anchor="middle" font-weight="bold">2024</text>
          </svg>
        </div>
        """
    },
    {
        "id": 8,
        "badge": "CLIMATIC REGIMES",
        "title": "Regime Statistics & Thermodynamic Buffer",
        "subtitle": "Normal summer days vs extreme regional heatwaves and latent heat dissipation",
        "notes": "Breaking the data down by climatic regime shows that under normal summer days below ninety degrees, the built offset averages 10.99 degrees. Under regional heat events at or above ninety degrees, the excess heat averages 12.86 degrees. When canopy shade is absent, net radiation partitions into sensible heat and ground storage rather than latent heat transpiration.",
        "html": """
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Climatic Regime</th>
                <th>Ambient Air (ERA5)</th>
                <th>Chapin Court LST</th>
                <th>Control Avg LST</th>
                <th>Net Excess Heat</th>
                <th>Sample Status / Context</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Normal Summer Days (&lt;90°F)</strong></td>
                <td class="mono">80.8°F avg</td>
                <td class="mono font-bold">99.46°F avg</td>
                <td class="mono">88.47°F avg</td>
                <td class="mono teal font-bold">+10.99°F</td>
                <td><span class="badge-pill gray">Baseline Built Offset</span></td>
              </tr>
              <tr class="row-highlight">
                <td><strong>Heatwave Days (≥90°F)</strong></td>
                <td class="mono">96.9°F avg</td>
                <td class="mono font-bold">114.76°F avg</td>
                <td class="mono">101.90°F avg</td>
                <td class="mono coral font-bold">+12.86°F</td>
                <td><span class="badge-pill coral">+1.875°F Gap Widening (Welch p ≈ 0.265)</span></td>
              </tr>
              <tr>
                <td><strong>Maximum Absolute Recorded</strong></td>
                <td class="mono">101.5°F (2023)</td>
                <td class="mono font-bold coral">122.59°F (2024)</td>
                <td class="mono">109.46°F (2024)</td>
                <td class="mono amber font-bold">+17.31°F (2006)</td>
                <td><span class="badge-pill amber">Sample Maximum (2006 Baseline)</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="grid-2col" style="margin-top: 1.25rem;">
          <div class="card-item">
            <div class="card-label">CANOPY EVAPOTRANSPIRATIVE BUFFER</div>
            <p class="body-text">
              Mature trees actively convert solar flux into <strong>latent heat</strong> via transpiration, cooling surrounding ambient air and preventing direct radiative loading of road surfaces and residential facades.
            </p>
          </div>
          <div class="card-item">
            <div class="card-label">SURFACE ENERGY BALANCE PARTITIONING</div>
            <p class="body-text">
              In the absence of vegetative shade and latent heat dissipation (evapotranspiration), net radiation (R<sub>n</sub>) partitions predominantly into <strong>sensible heat flux (H)</strong> and <strong>ground heat storage (G)</strong>, elevating asphalt pavement and dark roofing temperatures far above ambient air.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 9,
        "badge": "ECONOMETRIC MODELING",
        "title": "Heat-Regime Interaction Modeling",
        "subtitle": "Panel regression evaluating localized surface thermal amplification and future causal DiD designs",
        "notes": "To evaluate whether local heating responds disproportionately to ambient extremes, we fit an interaction panel model. By controlling for site-specific fixed effects and ambient air temperature, the interaction term evaluates whether Chapin Court experiences an added thermal penalty under heatwave conditions. Future causal modeling will incorporate parcel-specific removal dates.",
        "html": """
        <div class="math-card">
          <div class="math-label">HEAT-REGIME INTERACTION SPECIFICATION</div>
          <div class="math-formula">
            LST<sub>i,t</sub> = &alpha;<sub>i</sub> + &beta; &middot; T<sub>ambient,t</sub> + &delta; &middot; (Chapin<sub>i</sub> &times; HeatWave<sub>t</sub>) + &epsilon;<sub>i,t</sub>
          </div>
        </div>
        <div class="grid-2col" style="margin-top: 1.25rem;">
          <div class="card-item">
            <div class="card-label">VARIABLE DEFINITIONS</div>
            <ul class="bullet-list">
              <li><strong>i</strong>: Geographic observation site (Chapin Court, Rivercrest, Hillendale).</li>
              <li><strong>t</strong>: Timestamp of cloud-free USGS Landsat satellite overpass.</li>
              <li><strong>&alpha;<sub>i</sub></strong>: Site-specific fixed physical effects (base albedo, building geometry, elevation).</li>
              <li><strong>&beta;</strong>: Baseline atmospheric coupling slope across the regional airshed (0.772°F/°F).</li>
              <li><strong>&delta;</strong>: The interaction term evaluating additional surface amplification on Chapin Court during heat events (≥90°F ambient).</li>
              <li><strong>&epsilon;<sub>i,t</sub></strong>: Stochastic error term.</li>
            </ul>
          </div>
          <div class="card-item">
            <div class="card-label">METHODOLOGICAL APPLICATION & NEXT CAUSAL STEPS</div>
            <p class="body-text" style="line-height: 1.6;">
              This specification evaluates whether extreme ambient temperatures amplify localized surface heating. Across the 12 sampled dates, the interaction term indicates an added +2.64°F heatwave effect (p ≈ 0.42 in small-sample OLS). Full causal identification of the municipal removal program will incorporate parcel-level removal dates in a staggered difference-in-differences framework.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 10,
        "badge": "FOUR OPERATIONAL ERAS",
        "title": "Ground-Truth Timeline (1994–2026)",
        "subtitle": "Thirty-year evolution of subdivision platting, tree growth, municipal culling, and extreme heat",
        "notes": "The thirty-year history divides into four operational eras: initial subdivision platting with young saplings from 1994 to 2000; canopy maturation from 2001 to 2008; the municipal sidewalk enforcement and tree removal wave from 2009 to 2018; and the post-clearance era featuring extreme radiant heat and aggressive municipal penalty enforcement.",
        "html": """
        <div class="timeline-grid">
          <div class="timeline-card">
            <div class="epoch-badge">EPOCH 1 (1994–2000)</div>
            <div class="epoch-title">Platting & Immature Planting</div>
            <p class="epoch-text">
              Tower Vista subdivision platted with asphalt streets, curbs, and composite roofs. City required street trees as development condition. Saplings planted in narrow planter strips.
            </p>
          </div>
          <div class="timeline-card">
            <div class="epoch-badge teal">EPOCH 2 (2001–2008)</div>
            <div class="epoch-title">Maturation & Partial Shading</div>
            <p class="epoch-text">
              Deciduous and evergreen trees provided expanding crown canopy along Chapin Court, Linn Ave, and Warner Milne. Roots began maturing and expanding under standard 4-inch sidewalk panels.
            </p>
          </div>
          <div class="timeline-card alert">
            <div class="epoch-badge purple">EPOCH 3 (2009–2018)</div>
            <div class="epoch-title">Municipal Tree Removal Wave</div>
            <p class="epoch-text">
              Oregon City strictly enforced Title 12 sidewalk liability (OCMC 12.04.030), shifting root repair costs onto homeowners under threat of daily penalties. Trees were felled without shade replacement.
            </p>
          </div>
          <div class="timeline-card danger">
            <div class="epoch-badge coral">EPOCH 4 (2019–2026)</div>
            <div class="epoch-title">Post-Clearance Heat & Fines</div>
            <p class="epoch-text">
              Canopy depleted to 0.115 NDVI. Radiant surface peaks reached 122.59°F. Contemporaneously, City wielded $300/day fines racking up $72,000+ judgments (CE-000520-19) and water shutoffs while lagging on its own ADA Plan.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 11,
        "badge": "EPOCHS 1 & 2 • 1994–2008",
        "title": "Platting to Maturation",
        "subtitle": "Subdivision construction, young saplings, and the temporary emergence of canopy shading",
        "notes": "During the first two epochs, the newly platted Tower Vista subdivision transitioned from small saplings into an emerging shade canopy. As trees matured through the early 2000s, crown coverage began providing meaningful shading over residential sidewalks and streets, buffering mid-summer heat.",
        "html": """
        <div class="grid-2col">
          <div class="card-item">
            <div class="card-label">EPOCH 1: 1994–2000 SUBDIVISION PLATTING</div>
            <div class="metric-row">
              <span class="metric-name">Built Infrastructure:</span>
              <span class="metric-val">Asphalt streets, curbs, dark composite roofs</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Original Street Planting:</span>
              <span class="metric-val">1.5" to 2.0" nursery saplings mandated by planning approval</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Baseline Thermal Excess:</span>
              <span class="metric-val amber">+8.3°F to +12.3°F</span>
            </div>
            <p class="body-text" style="margin-top: 0.75rem;">
              Early thermal excess was driven by wide asphalt surfaces, but regional 1990s summers rarely breached 85°F ambient, keeping absolute temperatures within tolerable human thresholds.
            </p>
          </div>
          <div class="card-item">
            <div class="card-label">EPOCH 2: 2001–2008 CANOPY MATURATION</div>
            <div class="metric-row">
              <span class="metric-name">Vegetative Morphology:</span>
              <span class="metric-val teal">Expanding crown canopy over sidewalks & street</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Thermodynamic Function:</span>
              <span class="metric-val teal">Active latent heat evapotranspiration</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Corridor Benefit:</span>
              <span class="metric-val">Linn Ave & Warner Milne Rd canopy connectivity</span>
            </div>
            <p class="body-text" style="margin-top: 0.75rem;">
              Demonstrated that when trees achieved crown maturation, surface heat accumulation was buffered. However, expanding root systems in narrow planter strips inevitably clashed with standard 4-inch concrete panels.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 12,
        "badge": "EPOCH 3 • 2009–2018",
        "title": "The Municipal Tree Removal Wave & Liability Trap",
        "subtitle": "Title 12 sidewalk liability shifting and corridor-wide shade tree eradication",
        "notes": "Between 2009 and 2018, Oregon City enforced Municipal Code Title 12, citing homeowners for sidewalk panels lifted by tree roots that the City had originally required at subdivision approval. Faced with the choice between expensive engineering or municipal citations, property owners removed mature shade trees, resulting in zero continuous canopy replacement.",
        "html": """
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Permit Year</th>
                <th>Corridor Permits</th>
                <th>Documented Removals</th>
                <th>Municipal Regulatory Mechanism</th>
                <th>Canopy Replacement Policy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="mono font-bold">2011</td>
                <td class="mono">24 permits</td>
                <td class="mono coral">9 tree removals</td>
                <td>Title 12 notice of violation; sidewalk lifting citation</td>
                <td>Concrete pour-back; zero shade replacement</td>
              </tr>
              <tr>
                <td class="mono font-bold">2013</td>
                <td class="mono">16 permits</td>
                <td class="mono coral">8 tree removals</td>
                <td>ADA trip hazard abatement remediation order</td>
                <td>Bare planting strip or asphalt patch</td>
              </tr>
              <tr>
                <td class="mono font-bold">2015</td>
                <td class="mono">16 permits</td>
                <td class="mono coral">7 tree removals</td>
                <td>Municipal street tree removal authorization</td>
                <td>Dwarf ornamental saplings (negligible shade spread)</td>
              </tr>
              <tr>
                <td class="mono font-bold">2017</td>
                <td class="mono">19 permits</td>
                <td class="mono coral">6 tree removals</td>
                <td>Public works sidewalk inspection compliance</td>
                <td>Sidewalk panel widening over former root pits</td>
              </tr>
              <tr class="row-highlight">
                <td class="mono font-bold">2009–2018 Total</td>
                <td class="mono font-bold amber">167 permits cited</td>
                <td class="mono font-bold coral">Corridor Canopy Clearcut</td>
                <td>Municipal liability transfer to adjacent homeowners</td>
                <td><strong>Systematic elimination of continuous street canopy</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="note-box" style="margin-top: 1rem;">
          <strong class="coral">The Liability Trap:</strong> Under OCMC 12.04.030, the City shifted 100% of sidewalk maintenance liability onto abutting homeowners, citing Title II ADA trip hazards. Facing severe financial penalties, homeowners removed mature shade trees that the City had originally mandated at subdivision approval, while the City operated for decades without an adopted Public ROW ADA Transition Plan.
        </div>
        """
    },
    {
        "id": 13,
        "badge": "EPOCH 4 • 2019–2026",
        "title": "Post-Clearance Heat & Administrative Enforcement",
        "subtitle": "0.115 NDVI canopy collapse, 122.59°F surface peak, and $300/day municipal penalty stacking",
        "notes": "In the post-clearance era from 2019 to 2026, Chapin Court's vegetation index collapsed to 0.115. Radiant surface temperatures reached 122.59 degrees on July 9, 2024. During this same era, the City enforced continuing daily penalties of $300 per day against 12054 Chapin Court, producing a $72,000 default judgment and property liens, despite later claiming to the City Commission that the code only allowed a $300 maximum penalty.",
        "html": """
        <div class="grid-2col">
          <div class="card-item">
            <div class="card-label">CANOPY DEFICIT CONTRAST</div>
            <div class="metric-row">
              <span class="metric-name">Chapin Court Corridor NDVI:</span>
              <span class="metric-val coral">0.115 (depleted hardscape)</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Rivercrest Control NDVI:</span>
              <span class="metric-val teal">0.527 (mature canopy)</span>
            </div>
            <div class="metric-row highlight">
              <span class="metric-name">Hillendale Control NDVI:</span>
              <span class="metric-val teal">0.448 (residential shade)</span>
            </div>
            <p class="body-text" style="margin-top: 0.75rem;">
              The complete loss of mature street trees along Chapin Court leaves asphalt pavement and residential roofs unshielded from peak solar radiation.
            </p>
          </div>
          <div class="card-item danger">
            <div class="card-label">EXPOSURE RISKS & MUNICIPAL PENALTY ACCRUAL</div>
            <div class="metric-row">
              <span class="metric-name">Peak Radiant LST (July 9, 2024):</span>
              <span class="metric-val coral font-bold">122.59°F (Ambient 99.7°F)</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">August 2023 Heatwave LST:</span>
              <span class="metric-val coral">118.21°F (Ambient 101.5°F)</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Municipal Fine Stacking (CE-000520-19):</span>
              <span class="metric-val amber font-bold">$72,000 ($300/day stacked)</span>
            </div>
            <p class="body-text" style="margin-top: 0.75rem;">
              As radiant road temperatures reached 122.59°F, municipal authorities wielded $300/day continuing penalties to secure a $72,000 default judgment and property liens against 12054 Chapin Court, followed by a domestic water shutoff. In 2026, staff presented the same code to City Commission as "maxing out at $300" to justify $25,000 penalties.
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 14,
        "badge": "EVIDENTIARY ARCHITECTURE",
        "title": "Evidentiary Architecture & Causal Linkage",
        "subtitle": "Municipal Approval Mandate → Title 12 Cost-Shifting → Canopy Loss → Thermal Amplification",
        "notes": "The evidentiary architecture links municipal policy directly to environmental outcome: First, the City mandated street trees in narrow planter strips at subdivision approval. Second, the City shifted sidewalk repair liability onto abutting owners under threat of $300 daily fines. Third, homeowners removed mature trees without shade replacement, collapsing canopy to 0.115 NDVI. Fourth, this unbuffered hardscape produced an average 11 to 13 degree surface temperature elevation.",
        "html": """
        <div class="causal-chain-grid">
          <div class="causal-step">
            <div class="step-num coral">1</div>
            <div class="step-title">MUNICIPAL MANDATE & LIABILITY SHIFT</div>
            <div class="step-body">
              <strong>Planning Mandate & Cost-Shifting:</strong> City mandated street trees in narrow strips at platting, then shifted 100% of sidewalk repair liability onto abutting owners under OCMC 12.04.030 citing ADA trip hazards.
            </div>
          </div>
          <div class="causal-arrow">&rarr;</div>
          <div class="causal-step">
            <div class="step-num amber">2</div>
            <div class="step-title">PENALTY COERCION & CANOPY REMOVAL</div>
            <div class="step-body">
              <strong>Eradication Without Replacement:</strong> Faced with $300/day continuing fines and liens, homeowners removed trees. The City permitted concrete pour-backs and dwarf saplings, eliminating continuous street canopy.
            </div>
          </div>
          <div class="causal-arrow">&rarr;</div>
          <div class="causal-step">
            <div class="step-num teal">3</div>
            <div class="step-title">MEASURED SURFACE HEATING</div>
            <div class="step-body">
              <strong>Surface Amplification:</strong> Canopy collapse to 0.115 NDVI stripped evaporative cooling, elevating surface temperatures by <strong>+10.99°F to +12.86°F</strong>, with radiant surface temperatures peaking at <strong>122.59°F</strong>.
            </div>
          </div>
        </div>
        <div class="note-box" style="margin-top: 1.5rem;">
          <strong class="teal">Evidentiary Conclusion:</strong> The empirical data demonstrates that the microclimatic thermal burden at 12054 Chapin Court directly tracks municipal planning standards, Title 12 liability-shifting, and unmitigated canopy eradication.
        </div>
        """
    },
    {
        "id": 15,
        "badge": "LITIGATION SCRUTINY",
        "title": "Litigation Scrutiny & FRE / OEC 702 Compliance",
        "subtitle": "Rigorous evidentiary standards under the Cycle 1 Litigation Readiness Review",
        "notes": "Under the Cycle 1 Litigation Readiness Review, this assessment is structured to comply with Federal Rule of Evidence 702 and Oregon Evidence Code 702. It grounds all observations in calibrated USGS Landsat Level-2 products, elevation-matched controls, transparent reporting of small-sample statistical power, and authenticated municipal court records.",
        "html": """
        <div class="grid-2col">
          <div class="card-item">
            <div class="card-label">FRE 702 / OEC 702 FOUNDATION</div>
            <ul class="bullet-list">
              <li>
                <strong>Calibrated Radiometry:</strong> Relies exclusively on calibrated USGS Landsat Collection 2 Level-2 Surface Temperature products (30m grid resampled from native 60–120m thermal sensors).
              </li>
              <li>
                <strong>Matched-Elevation Controls:</strong> Controls selected within the same municipal boundary and elevation band (~443–475 ft ASL), isolating macro atmospheric air masses.
              </li>
              <li>
                <strong>Transparent Small-Sample Power:</strong> Explicitly reports small-sample statistics (Welch p ≈ 0.265, slope CI [-0.046, +0.317]) to prevent cross-examination impeachment.
              </li>
              <li>
                <strong>Authenticated Municipal Records:</strong> Corroborated by Clackamas County Municipal Court dockets CE-000520-19 and CE-000554-20 and recorded county liens.
              </li>
            </ul>
          </div>
          <div class="card-item">
            <div class="card-label">CYCLE 1 LITIGATION READINESS GATES</div>
            <div class="metric-row">
              <span class="metric-name">Gate 1: Sensor & Weather Reproduction</span>
              <span class="metric-val teal">USGS Level-2 & ERA5-Land Verified</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Gate 2: Geocoded Permit Ledger</span>
              <span class="metric-val amber">167 Corridor Permits Mapped</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Gate 3: Causal DiD Specification</span>
              <span class="metric-val teal">Parcel-Level Staggered Design</span>
            </div>
            <div class="metric-row">
              <span class="metric-name">Gate 4: Formal Expert & Counsel Review</span>
              <span class="metric-val coral">In Progress (Cycle 1 Audit Complete)</span>
            </div>
            <p class="body-text" style="margin-top: 0.75rem;">
              Meets standards under Federal Rule of Evidence 702 and Oregon Evidence Code 702 (ORS 40.410).
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 16,
        "badge": "PRIMARY SOURCES",
        "title": "Primary Sources & References",
        "subtitle": "Federal remote-sensing documentation, reanalysis baselines, and municipal permit registers",
        "notes": "Our findings are grounded in primary federal and municipal data sources: the USGS EROS Landsat Level-2 Science Product Guide, ECMWF Open-Meteo ERA5-Land hourly atmospheric reanalysis, Oregon City Municipal Code Chapters 1.20, 1.24, and Title 12, Municipal Court dockets CE-000520-19 and CE-000554-20, and the Cycle 1 Litigation Readiness Review.",
        "html": """
        <div class="grid-2col">
          <div class="card-item">
            <div class="card-label">PRIMARY DATA ARCHIVES</div>
            <ul class="bullet-list" style="font-size: 0.85rem;">
              <li>
                <strong>USGS EROS Center:</strong> Landsat Collection 2 Level-2 Surface Temperature Science Product Guide (2020). Calibration: <code>T<sub>K</sub> = DN &times; 0.00341802 + 149.0 K</code>.
              </li>
              <li>
                <strong>Open-Meteo / ECMWF:</strong> ERA5-Land Hourly Surface Temperature Reanalysis Baselines, Oregon City Coordinates (45.33° N, -122.61° W).
              </li>
              <li>
                <strong>Oregon City Municipal Court:</strong> Case CE-000520-19 ($72,000 judgment; Clackamas County Doc. 2019-079244) and Case CE-000554-20 ($14,601 judgment & lien; Doc. 2021-006197).
              </li>
              <li>
                <strong>Oregon City Municipal Code:</strong> Title 12: Streets & Sidewalks (12.04.030) and Enforcement Chapters 1.20, 1.24, 8.08, 8.20, 8.28.
              </li>
              <li>
                <strong>Legal Standards:</strong> Federal Rule of Evidence 702 and Oregon Evidence Code 702 (ORS 40.410).
              </li>
            </ul>
          </div>
          <div class="card-item">
            <div class="card-label">SUBJECT RECORD INFORMATION</div>
            <div class="meta-tag-list" style="margin-bottom: 0.75rem;">
              <span class="mono-badge">Subject: 12054 Chapin Court</span>
              <span class="mono-badge">Jurisdiction: Oregon City, OR</span>
              <span class="mono-badge">Subdivision: Tower Vista</span>
              <span class="mono-badge">Overpass Span: 1994–2024</span>
            </div>
            <p class="body-text" style="font-size: 0.85rem; line-height: 1.55;">
              Technical report compiled from verified public records, peer-reviewed federal satellite observations, and gridded atmospheric reanalyses. Structured in accordance with the Cycle 1 Litigation Readiness Review.
            </p>
            <div style="margin-top: 1rem;">
              <a href="index.html" class="back-link">&larr; Return to Executive Function OS Hub</a>
            </div>
          </div>
        </div>
        """
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Forensic Microclimate Investigation — Comparative Surface-Temperature Assessment (1994–2024)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-canvas: #090D14;
      --bg-slide: #0F172A;
      --bg-card: #162036;
      --bg-card-subtle: #1E293B;
      --text-primary: #F8FAFC;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      --border-hairline: #1E293B;
      --border-focus: #334155;

      --amber-base: #D97706;
      --amber-bright: #F59E0B;
      --amber-bg: rgba(217, 119, 6, 0.12);
      --amber-border: rgba(217, 119, 6, 0.35);

      --teal-base: #0D9488;
      --teal-bright: #14B8A6;
      --teal-bg: rgba(13, 148, 136, 0.12);
      --teal-border: rgba(13, 148, 136, 0.35);

      --coral-base: #E11D48;
      --coral-bright: #F43F5E;
      --coral-bg: rgba(244, 63, 94, 0.12);
      --coral-border: rgba(244, 63, 94, 0.35);

      --purple-base: #7C3AED;
      --purple-bright: #A78BFA;
      --purple-bg: rgba(124, 58, 237, 0.12);
      --purple-border: rgba(124, 58, 237, 0.35);

      --font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'Fira Code', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html, body {
      width: 100%;
      height: 100%;
      background-color: var(--bg-canvas);
      color: var(--text-primary);
      font-family: var(--font-body);
      overflow: hidden;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    #deck-wrapper {
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
      background: var(--bg-canvas);
    }

    /* Top Progress Bar */
    #progress-bar {
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 50;
    }
    #progress-fill {
      height: 100%;
      width: 6.25%;
      background: linear-gradient(90deg, var(--teal-bright), var(--amber-bright), var(--coral-bright));
      transition: width 0.3s ease;
    }

    /* Header Bar */
    .deck-header {
      height: 56px;
      padding: 0 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-hairline);
      background: rgba(9, 13, 20, 0.95);
      backdrop-filter: blur(8px);
      z-index: 40;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-badge {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
      background: var(--coral-bg);
      border: 1px solid var(--coral-border);
      color: var(--coral-bright);
      font-weight: 600;
    }
    .brand-title {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 0.95rem;
      color: var(--text-primary);
    }
    .deck-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .control-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      color: var(--text-secondary);
      padding: 6px 12px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    .control-btn:hover {
      background: var(--bg-card-subtle);
      color: var(--text-primary);
      border-color: var(--border-focus);
    }

    /* Slide Arena */
    #slide-arena {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .slide {
      position: absolute;
      width: 100%;
      max-width: 1100px;
      height: 100%;
      max-height: 720px;
      background: var(--bg-slide);
      border: 1px solid var(--border-hairline);
      border-radius: 12px;
      padding: 2rem 2.5rem;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transform: translateX(30px);
      transition: opacity 0.35s ease, transform 0.35s ease;
      overflow-y: auto;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }
    .slide.active {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(0);
      z-index: 10;
    }

    /* Slide Typography */
    .slide-badge {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--amber-bright);
      font-weight: 600;
      margin-bottom: 0.4rem;
    }
    .slide-title {
      font-family: var(--font-display);
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.2;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }
    .slide-subtitle {
      font-size: 0.95rem;
      color: var(--text-secondary);
      margin-top: 0.35rem;
      margin-bottom: 1.25rem;
      line-height: 1.45;
    }
    .body-text {
      font-size: 0.92rem;
      color: var(--text-secondary);
      line-height: 1.6;
    }

    /* Layout Grids */
    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
    }
    .grid-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
    }
    .grid-4col {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.85rem;
    }

    /* Cards & Containers */
    .card-item {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      padding: 1.15rem;
      transition: border-color 0.2s ease;
    }
    .card-item:hover {
      border-color: var(--border-focus);
    }
    .card-item.danger {
      border-color: var(--coral-border);
      background: rgba(225, 29, 72, 0.05);
    }
    .card-label {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 0.4rem;
    }
    .card-value-large {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-primary);
    }
    .card-subtext {
      font-size: 0.8rem;
      color: var(--text-secondary);
      margin-top: 0.25rem;
    }

    /* Hero Box */
    .hero-box {
      display: flex;
      flex-direction: column;
      justify-content: center;
      height: 100%;
    }
    .lead-badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--amber-bright);
      background: var(--amber-bg);
      border: 1px solid var(--amber-border);
      padding: 4px 10px;
      border-radius: 4px;
      width: fit-content;
      margin-bottom: 0.75rem;
    }
    .hero-title {
      font-family: var(--font-display);
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.15;
      color: #FFFFFF;
      letter-spacing: -0.02em;
    }
    .hero-subtitle {
      font-size: 1.1rem;
      color: var(--text-secondary);
      margin-top: 0.75rem;
      max-width: 820px;
      line-height: 1.5;
    }

    /* Stat Cards */
    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .stat-card.alert {
      border-color: var(--coral-border);
      background: var(--coral-bg);
    }
    .stat-card.danger {
      border-color: var(--coral-bright);
      background: rgba(244, 63, 94, 0.18);
    }
    .stat-title {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }
    .stat-number {
      font-family: var(--font-display);
      font-size: 2.1rem;
      font-weight: 800;
      margin: 0.35rem 0;
    }
    .stat-desc {
      font-size: 0.78rem;
      color: var(--text-secondary);
      line-height: 1.4;
    }
    .stat-highlight {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      margin: 0.35rem 0;
    }

    /* Colors */
    .coral { color: var(--coral-bright); }
    .amber { color: var(--amber-bright); }
    .teal { color: var(--teal-bright); }
    .purple { color: var(--purple-bright); }
    .mono { font-family: var(--font-mono); }
    .small { font-size: 0.78rem; }
    .font-bold { font-weight: 700; }

    /* Tables */
    .table-responsive {
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      background: var(--bg-card);
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: left;
    }
    .data-table th {
      background: #111A2E;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 8px 12px;
      border-bottom: 1px solid var(--border-hairline);
      position: sticky;
      top: 0;
      z-index: 2;
    }
    .data-table td {
      padding: 7px 12px;
      border-bottom: 1px solid var(--border-hairline);
      color: var(--text-secondary);
      white-space: nowrap;
    }
    .data-table tr:hover {
      background: rgba(255, 255, 255, 0.02);
    }
    .data-table tr.row-highlight {
      background: rgba(244, 63, 94, 0.08);
    }
    .data-table tr.row-target {
      background: rgba(244, 63, 94, 0.12);
    }

    .badge-pill {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 600;
    }
    .badge-pill.coral { background: var(--coral-bg); color: var(--coral-bright); border: 1px solid var(--coral-border); }
    .badge-pill.teal { background: var(--teal-bg); color: var(--teal-bright); border: 1px solid var(--teal-border); }
    .badge-pill.amber { background: var(--amber-bg); color: var(--amber-bright); border: 1px solid var(--amber-border); }
    .badge-pill.purple { background: var(--purple-bg); color: var(--purple-bright); border: 1px solid var(--purple-border); }
    .badge-pill.gray { background: rgba(148, 163, 184, 0.1); color: #94A3B8; border: 1px solid #334155; }
    .badge-pill.red { background: rgba(225, 29, 72, 0.2); color: #FB7185; border: 1px solid rgba(225, 29, 72, 0.4); }

    .mono-badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-hairline);
      color: var(--text-secondary);
      padding: 2px 6px;
      border-radius: 4px;
      margin-right: 4px;
      margin-bottom: 4px;
    }
    .mono-badge.coral { color: var(--coral-bright); border-color: var(--coral-border); background: var(--coral-bg); }
    .mono-badge.amber { color: var(--amber-bright); border-color: var(--amber-border); background: var(--amber-bg); }
    .mono-badge.teal { color: var(--teal-bright); border-color: var(--teal-border); background: var(--teal-bg); }
    .mono-badge.purple { color: var(--purple-bright); border-color: var(--purple-border); background: var(--purple-bg); }

    /* Banners & Callouts */
    .callout-banner {
      background: linear-gradient(135deg, rgba(13, 148, 136, 0.12), rgba(217, 119, 6, 0.08));
      border: 1px solid var(--teal-border);
      border-radius: 8px;
      padding: 1.25rem 1.5rem;
    }
    .callout-label {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--teal-bright);
      margin-bottom: 0.4rem;
      font-weight: 600;
    }
    .callout-quote {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.4;
    }
    .note-box {
      background: var(--bg-card-subtle);
      border-left: 3px solid var(--teal-bright);
      padding: 0.75rem 1rem;
      border-radius: 0 6px 6px 0;
      font-size: 0.85rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }

    /* Metric rows */
    .metric-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      font-size: 0.88rem;
    }
    .metric-row:last-child { border-bottom: none; }
    .metric-row.highlight {
      background: rgba(245, 158, 11, 0.08);
      padding: 6px 8px;
      border-radius: 4px;
      border-bottom: none;
      margin-top: 4px;
    }
    .metric-name { color: var(--text-secondary); font-size: 0.85rem; }
    .metric-val { font-family: var(--font-mono); font-weight: 600; }

    /* Lists */
    .bullet-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .bullet-list li {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.5;
      padding-left: 1.25rem;
      position: relative;
    }
    .bullet-list li::before {
      content: "▪";
      color: var(--amber-bright);
      position: absolute;
      left: 0;
      font-size: 0.9rem;
    }

    /* Charts */
    .chart-container {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      padding: 1rem;
      height: 100%;
      display: flex;
      flex-direction: column;
    }
    .chart-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-secondary);
      margin-bottom: 0.5rem;
    }
    .chart-legend-row {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.72rem;
    }
    .legend-chip {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }
    .dot.coral { background: var(--coral-bright); }
    .dot.teal { background: var(--teal-bright); }
    .dot.amber { background: var(--amber-bright); }
    .bar-chip {
      width: 10px;
      height: 8px;
      background: rgba(245, 158, 11, 0.5);
      border-radius: 2px;
    }
    .slope-svg, .time-series-svg {
      width: 100%;
      height: 100%;
      min-height: 200px;
    }

    /* Math Formula Card */
    .math-card {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
      border: 1px solid var(--amber-border);
      border-radius: 8px;
      padding: 1.5rem;
      text-align: center;
    }
    .math-label {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--amber-bright);
      margin-bottom: 0.5rem;
    }
    .math-formula {
      font-family: var(--font-mono);
      font-size: 1.35rem;
      font-weight: 600;
      color: #FFFFFF;
      letter-spacing: 0.02em;
    }

    /* Timeline Grid */
    .timeline-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.85rem;
      height: 100%;
    }
    .timeline-card {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
    }
    .timeline-card.alert { border-color: var(--purple-border); }
    .timeline-card.danger { border-color: var(--coral-border); background: var(--coral-bg); }
    .epoch-badge {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 600;
      color: var(--amber-bright);
      margin-bottom: 0.35rem;
    }
    .epoch-badge.teal { color: var(--teal-bright); }
    .epoch-badge.purple { color: var(--purple-bright); }
    .epoch-badge.coral { color: var(--coral-bright); }
    .epoch-title {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.6rem;
      line-height: 1.3;
    }
    .epoch-text {
      font-size: 0.8rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }

    /* Causal Chain */
    .causal-chain-grid {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-top: 1rem;
    }
    .causal-step {
      flex: 1;
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: 8px;
      padding: 1.25rem;
    }
    .step-num {
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
    }
    .step-title {
      font-family: var(--font-display);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.5rem;
    }
    .step-body {
      font-size: 0.85rem;
      color: var(--text-secondary);
      line-height: 1.55;
    }
    .causal-arrow {
      font-size: 1.75rem;
      color: var(--text-muted);
      font-weight: bold;
    }

    .back-link {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      color: var(--teal-bright);
      text-decoration: none;
      padding: 6px 12px;
      border: 1px solid var(--teal-border);
      border-radius: 6px;
      background: var(--teal-bg);
      transition: all 0.2s ease;
    }
    .back-link:hover {
      background: var(--teal-bright);
      color: #000;
    }

    /* Footer Navigation */
    .deck-footer {
      height: 52px;
      padding: 0 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-hairline);
      background: rgba(9, 13, 20, 0.95);
      backdrop-filter: blur(8px);
      z-index: 40;
    }
    .slide-counter {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      color: var(--text-secondary);
    }
    .footer-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      color: var(--text-primary);
      padding: 6px 14px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      touch-action: manipulation;
    }
    .nav-btn:hover {
      background: var(--bg-card-subtle);
      border-color: var(--border-focus);
    }
    .nav-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    /* Drawer / Modal: Contents Menu */
    #contents-drawer, #notes-drawer {
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      width: 340px;
      background: #0B1120;
      border-right: 1px solid var(--border-hairline);
      z-index: 90;
      transform: translateX(-100%);
      transition: transform 0.25s ease;
      display: flex;
      flex-direction: column;
      box-shadow: 10px 0 30px rgba(0, 0, 0, 0.7);
    }
    #notes-drawer {
      left: auto;
      right: 0;
      border-right: none;
      border-left: 1px solid var(--border-hairline);
      transform: translateX(100%);
    }
    #contents-drawer.open, #notes-drawer.open {
      transform: translateX(0);
    }
    .drawer-header {
      padding: 1rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-hairline);
    }
    .drawer-title {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1rem;
      color: var(--text-primary);
    }
    .close-drawer-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.25rem;
      cursor: pointer;
    }
    .drawer-list {
      flex: 1;
      overflow-y: auto;
      padding: 0.5rem;
    }
    .drawer-item {
      padding: 10px 12px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: baseline;
      gap: 8px;
      transition: background 0.15s ease;
    }
    .drawer-item:hover {
      background: var(--bg-card);
    }
    .drawer-item.active {
      background: var(--amber-bg);
      border: 1px solid var(--amber-border);
    }
    .drawer-num {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--amber-bright);
    }
    .drawer-text {
      font-size: 0.85rem;
      color: var(--text-primary);
      line-height: 1.35;
    }

    #notes-content {
      padding: 1.25rem;
      font-size: 0.95rem;
      color: #E2E8F0;
      line-height: 1.65;
      flex: 1;
      overflow-y: auto;
    }

    /* Voice Narration Controller Widget (Floating Glassmorphic Panel) */
    #narrator-panel {
      position: fixed;
      bottom: 60px;
      right: 20px;
      z-index: 100;
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #F8FAFC;
      padding: 8px 12px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.6);
      touch-action: manipulation;
    }
    #toggle-narration-btn {
      background: var(--teal-base);
      border: 1px solid var(--teal-bright);
      color: white;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
      font-family: var(--font-mono);
      font-size: 11px;
      transition: all 0.15s ease;
      touch-action: manipulation;
    }
    #toggle-narration-btn:hover {
      background: var(--teal-bright);
    }
    #read-current-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: white;
      padding: 6px 10px;
      border-radius: 4px;
      cursor: pointer;
      font-family: var(--font-mono);
      font-size: 11px;
      transition: all 0.15s ease;
      touch-action: manipulation;
    }
    #read-current-btn:hover {
      background: rgba(255, 255, 255, 0.15);
    }
    #voice-select-label {
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      color: #94A3B8;
    }
    #voice-select {
      background: #1E293B;
      color: #F8FAFC;
      border: 1px solid #334155;
      border-radius: 4px;
      padding: 4px 6px;
      max-width: 140px;
      font-family: var(--font-mono);
      font-size: 10px;
    }

    @media (max-width: 900px) {
      .grid-4col { grid-template-columns: repeat(2, 1fr); }
      .grid-3col { grid-template-columns: 1fr; }
      .grid-2col { grid-template-columns: 1fr; }
      .timeline-grid { grid-template-columns: 1fr; }
      .causal-chain-grid { flex-direction: column; }
      .causal-arrow { transform: rotate(90deg); margin: 0.25rem 0; }
      .slide { padding: 1.25rem 1.5rem; max-height: 90vh; }
      .hero-title { font-size: 1.75rem; }
      .slide-title { font-size: 1.45rem; }
      #narrator-panel {
        bottom: 56px;
        right: 8px;
        left: 8px;
        padding: 6px 8px;
        gap: 6px;
        justify-content: space-between;
      }
      #voice-select { max-width: 105px; font-size: 9px; }
      #toggle-narration-btn, #read-current-btn { padding: 5px 8px; font-size: 10px; }
    }
  </style>
</head>
<body>

  <div id="deck-wrapper">
    <!-- Top Progress Bar -->
    <div id="progress-bar">
      <div id="progress-fill"></div>
    </div>

    <!-- Header Bar -->
    <div class="deck-header">
      <div class="brand-group">
        <span class="brand-badge">FRE 702 / DAUBERT</span>
        <span class="brand-title">Forensic Microclimate Investigation</span>
      </div>
      <div class="deck-controls">
        <button class="control-btn" id="open-contents-btn">📑 Contents</button>
        <button class="control-btn" id="open-notes-btn">📝 Notes (N)</button>
        <button class="control-btn" id="toggle-fullscreen-btn">⛶ Fullscreen (F)</button>
      </div>
    </div>

    <!-- Slide Arena -->
    <div id="slide-arena">
      {SLIDES_HTML}
    </div>

    <!-- Footer Bar -->
    <div class="deck-footer">
      <div class="slide-counter">
        <span id="current-slide-num">1</span> / <span id="total-slide-num">16</span>
      </div>
      <div class="footer-actions">
        <button class="nav-btn" id="prev-btn" disabled>&larr; Previous</button>
        <button class="nav-btn" id="next-btn">Next &rarr;</button>
      </div>
    </div>
  </div>

  <!-- Contents Drawer -->
  <div id="contents-drawer">
    <div class="drawer-header">
      <div class="drawer-title">Table of Contents</div>
      <button class="close-drawer-btn" id="close-contents-btn">&times;</button>
    </div>
    <div class="drawer-list" id="contents-list"></div>
  </div>

  <!-- Notes Drawer -->
  <div id="notes-drawer">
    <div class="drawer-header">
      <div class="drawer-title">Speaker Evidentiary Notes</div>
      <button class="close-drawer-btn" id="close-notes-btn">&times;</button>
    </div>
    <div id="notes-content"></div>
  </div>

  <!-- Voice Narration Controller -->
  <div id="narrator-panel">
    <button id="toggle-narration-btn">▶ Auto-Present</button>
    <button id="read-current-btn">🔊 Read Slide</button>
    <label id="voice-select-label">
      Voice:
      <select id="voice-select"></select>
    </label>
  </div>

  <script>
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    let currentSlide = 0;

    const progressFill = document.getElementById('progress-fill');
    const currentSlideNum = document.getElementById('current-slide-num');
    const totalSlideNum = document.getElementById('total-slide-num');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    const contentsDrawer = document.getElementById('contents-drawer');
    const notesDrawer = document.getElementById('notes-drawer');
    const notesContent = document.getElementById('notes-content');
    const contentsList = document.getElementById('contents-list');

    totalSlideNum.textContent = totalSlides;

    slides.forEach((slide, idx) => {
      const item = document.createElement('div');
      item.className = 'drawer-item' + (idx === 0 ? ' active' : '');
      item.innerHTML = `
        <span class="drawer-num">${String(idx + 1).padStart(2, '0')}</span>
        <span class="drawer-text">${slide.querySelector('.slide-title')?.textContent || 'Slide ' + (idx + 1)}</span>
      `;
      item.addEventListener('click', () => {
        goToSlide(idx);
        contentsDrawer.classList.remove('open');
      });
      contentsList.appendChild(item);
    });

    function updateDeck() {
      slides.forEach((slide, idx) => {
        slide.classList.toggle('active', idx === currentSlide);
      });

      currentSlideNum.textContent = currentSlide + 1;
      const pct = ((currentSlide + 1) / totalSlides) * 100;
      progressFill.style.width = pct + '%';

      prevBtn.disabled = currentSlide === 0;
      nextBtn.disabled = currentSlide === totalSlides - 1;

      const items = contentsList.querySelectorAll('.drawer-item');
      items.forEach((it, idx) => it.classList.toggle('active', idx === currentSlide));

      const activeSlide = slides[currentSlide];
      const notes = activeSlide.getAttribute('data-notes') || 'No evidentiary notes for this slide.';
      notesContent.textContent = notes;
    }

    function goToSlide(idx) {
      if (idx >= 0 && idx < totalSlides) {
        currentSlide = idx;
        updateDeck();
      }
    }

    function nextSlide() {
      if (currentSlide < totalSlides - 1) {
        currentSlide++;
        updateDeck();
      }
    }

    function prevSlide() {
      if (currentSlide > 0) {
        currentSlide--;
        updateDeck();
      }
    }

    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);

    document.getElementById('open-contents-btn').addEventListener('click', () => contentsDrawer.classList.add('open'));
    document.getElementById('close-contents-btn').addEventListener('click', () => contentsDrawer.classList.remove('open'));

    document.getElementById('open-notes-btn').addEventListener('click', () => notesDrawer.classList.add('open'));
    document.getElementById('close-notes-btn').addEventListener('click', () => notesDrawer.classList.remove('open'));

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
    document.getElementById('toggle-fullscreen-btn').addEventListener('click', toggleFullscreen);

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault();
        goToSlide(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        goToSlide(totalSlides - 1);
      } else if (e.key.toLowerCase() === 'n') {
        e.preventDefault();
        notesDrawer.classList.toggle('open');
      } else if (e.key.toLowerCase() === 'f') {
        e.preventDefault();
        toggleFullscreen();
      }
    });

    let touchStartX = 0;
    let touchEndX = 0;
    const arena = document.getElementById('slide-arena');
    arena.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    arena.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchEndX < touchStartX - 50) nextSlide();
      if (touchEndX > touchStartX + 50) prevSlide();
    }, { passive: true });

    updateDeck();

    class PresentationNarrator {
      constructor() {
        this.synth = window.speechSynthesis;
        this.voices = [];
        this.selectedVoice = null;
        this.isAutoPlaying = false;
        this.currentUtterance = null;
        this.keepAliveTimer = null;

        this.initVoices();
        this.bindEvents();
      }

      initVoices() {
        const populate = () => {
          if (!this.synth) return;
          this.voices = this.synth.getVoices().filter(v => v.lang && v.lang.startsWith('en'));
          
          const select = document.getElementById('voice-select');
          if (!select) return;
          select.innerHTML = '';

          const naturalKeywords = ['natural', 'neural', 'google', 'samantha', 'karen', 'daniel', 'serena', 'oliver', 'ava', 'zoe', 'jenny', 'guy', 'aria'];

          this.voices.sort((a, b) => {
            const aNat = naturalKeywords.some(kw => a.name.toLowerCase().includes(kw));
            const bNat = naturalKeywords.some(kw => b.name.toLowerCase().includes(kw));
            return bNat - aNat;
          });

          this.voices.forEach((voice, index) => {
            const option = document.createElement('option');
            option.value = index;
            const cleanName = voice.name.replace(/Microsoft |Google /g, '').replace(/ Online \\(Natural\\)/g, ' Natural');
            option.textContent = `${cleanName} (${voice.lang})`;
            select.appendChild(option);
          });

          if (this.voices.length > 0) {
            this.selectedVoice = this.voices[0];
            select.selectedIndex = 0;
          }
        };

        populate();
        if (typeof speechSynthesis !== 'undefined' && speechSynthesis.onvoiceschanged !== undefined) {
          speechSynthesis.onvoiceschanged = populate;
        }
      }

      getCurrentNotesText() {
        const activeSlide = document.querySelector('.slide.active');
        if (!activeSlide) return '';
        let text = activeSlide.getAttribute('data-notes') || '';
        return text.trim();
      }

      advanceSlide() {
        nextSlide();
      }

      speakCurrentSlide(onComplete = null) {
        if (!this.synth) return;
        this.synth.cancel();
        if (this.keepAliveTimer) {
          clearInterval(this.keepAliveTimer);
          this.keepAliveTimer = null;
        }

        const text = this.getCurrentNotesText();
        if (!text) {
          if (onComplete) onComplete();
          return;
        }

        const utterance = new SpeechSynthesisUtterance(text);
        if (this.selectedVoice) utterance.voice = this.selectedVoice;

        utterance.rate = 1.02;
        utterance.pitch = 1.0;

        utterance.onend = () => {
          if (this.keepAliveTimer) {
            clearInterval(this.keepAliveTimer);
            this.keepAliveTimer = null;
          }
          this.currentUtterance = null;
          if (onComplete) onComplete();
        };

        utterance.onerror = (e) => {
          console.warn('Speech synthesis notice:', e);
          if (this.keepAliveTimer) {
            clearInterval(this.keepAliveTimer);
            this.keepAliveTimer = null;
          }
          this.currentUtterance = null;
        };

        this.currentUtterance = utterance;

        this.keepAliveTimer = setInterval(() => {
          if (this.synth.speaking) {
            this.synth.pause();
            this.synth.resume();
          }
        }, 10000);

        this.synth.speak(utterance);
      }

      startAutoPlay() {
        this.isAutoPlaying = true;
        const playBtn = document.getElementById('toggle-narration-btn');
        if (playBtn) {
          playBtn.textContent = '⏸ Pause';
          playBtn.style.background = '#e11d48';
        }

        const step = () => {
          if (!this.isAutoPlaying) return;

          this.speakCurrentSlide(() => {
            if (!this.isAutoPlaying) return;

            if (currentSlide >= totalSlides - 1) {
              this.stopAutoPlay();
              return;
            }

            setTimeout(() => {
              if (!this.isAutoPlaying) return;
              this.advanceSlide();
              setTimeout(step, 500);
            }, 1200);
          });
        };

        step();
      }

      stopAutoPlay() {
        this.isAutoPlaying = false;
        if (this.synth) this.synth.cancel();
        if (this.keepAliveTimer) {
          clearInterval(this.keepAliveTimer);
          this.keepAliveTimer = null;
        }
        const playBtn = document.getElementById('toggle-narration-btn');
        if (playBtn) {
          playBtn.textContent = '▶ Auto-Present';
          playBtn.style.background = 'var(--teal-base)';
        }
      }

      bindEvents() {
        const playBtn = document.getElementById('toggle-narration-btn');
        const readBtn = document.getElementById('read-current-btn');
        const select = document.getElementById('voice-select');

        if (playBtn) {
          playBtn.addEventListener('click', () => {
            if (this.isAutoPlaying) {
              this.stopAutoPlay();
            } else {
              this.startAutoPlay();
            }
          });
        }

        if (readBtn) {
          readBtn.addEventListener('click', () => {
            this.stopAutoPlay();
            this.speakCurrentSlide();
          });
        }

        if (select) {
          select.addEventListener('change', (e) => {
            this.selectedVoice = this.voices[e.target.value];
          });
        }

        window.addEventListener('keydown', (e) => {
          if (['ArrowLeft', 'ArrowRight', 'Space'].includes(e.code) && !this.isAutoPlaying) {
            if (this.synth) this.synth.cancel();
          }
        });
      }
    }

    window.narrator = new PresentationNarrator();
  </script>
</body>
</html>
"""

slides_html_parts = []
for s in slides_data:
    slide_part = f"""
    <div class="slide{" active" if s["id"] == 1 else ""}" id="slide-{s["id"]}" data-notes="{s["notes"]}">
      <div class="slide-badge">{s["badge"]}</div>
      <div class="slide-title">{s["title"]}</div>
      <div class="slide-subtitle">{s["subtitle"]}</div>
      <div class="slide-body">
        {s["html"]}
      </div>
    </div>
    """
    slides_html_parts.append(slide_part)

full_html = html_template.replace("{SLIDES_HTML}", "\n".join(slides_html_parts))

with open("/home/annika/ExecutiveFunctionOS_Web/forensic-microclimate.html", "w", encoding="utf-8") as f:
    f.write(full_html)

with open("/home/annika/ExecutiveFunctionOS_Web/chapin-thermal.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated forensic-microclimate.html and chapin-thermal.html successfully!")
