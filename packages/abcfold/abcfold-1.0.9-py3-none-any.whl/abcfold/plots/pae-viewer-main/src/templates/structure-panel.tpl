<template id="structure-panel-template">
  <div class="structure-panel">
    <div class="sp-description"></div>
    <details class="sp-crosslinks hidden">
      <summary><b>Crosslinks</b></summary>
      <div>
        Source:
        <a href="https://www.science.org/doi/10.1126/science.abb3758"
           target="_blank">O'Reilly <i>et al.</i> (2020)</a>
      </div>
      <div>
        <a class="sp-crosslinks-download"
           href="crosslinks/mycowiki_crosslinks.zip" download>
          <img src="{{@img/bootstrap-icons/download.svg}}"
               title="Download crosslink data">
          <span>
          Download structures, crosslink distances and
          PyMOL files for visualization
        </span>
        </a>
      </div>
      <div>
        <p class="sp-toggle-crosslinks-header">
          Show crosslinks:
        </p>
        <div class="sp-toggle-crosslinks">
          <label>
            <input type="checkbox" data-crosslinker="DSS"
                   autocomplete="off" checked>
            <span>DSS</span>
          </label>
        </div>

        <div class="sp-toggle-crosslinks">
          <label>
            <input type="checkbox" data-crosslinker="DSSO"
                   autocomplete="off" checked>
            <span>DSSO</span>
          </label>
        </div>
      </div>
      <div class="sp-toggle-distances">
        <label>
          <input type="checkbox" autocomplete="off">
          <span>Show only crosslinks that fit structure</span>
        </label>
      </div>
      <p>
        Crosslinks between residues are indicated by dashed lines.
        <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3137222/"
           target="_blank">Xwalk</a> was used for simulation of
        the actual crosslinkers, which are 3D rendered in cases
        where the crosslinks fit the displayed structure.
      </p>
    </details>
    <details class="sp-complex hidden">
      <summary><b>Complex</b></summary>
      <div class="sp-complex-source">
        <strong>Source</strong>:
        <a href="http://doi.org/10.15252/msb.202311544" target="_blank">O'Reilly <i>et al.</i> (2023)</a>
      </div>
      <div class="sp-chain-legend"></div>
      <div class="sp-metrics">
        <strong>Confidence metrics:</strong>
        <ul>
          <li>
          <span>
            Mean pLDDT<sup><a
              href="https://doi.org/10.1038/s41586-021-03819-2" target="_blank"
              title="Highly accurate protein structure prediction with AlphaFold (2021)">?</a></sup>:</span>
            <span class="sp-metric-value" data-type="plddt"></span></li>
          <li>
          <span>pTM<sup><a
              href="https://doi.org/10.1038/s41586-021-03819-2" target="_blank"
              title="Highly accurate protein structure prediction with AlphaFold (2021)">?</a></sup>:</span>
            <span class="sp-metric-value" data-type="ptm"></span></li>
          <li>
          <span>ipTM<sup><a
              href="https://doi.org/10.1101/2021.10.04.463034"
              target="_blank" title="Protein complex prediction with AlphaFold-Multimer (2022)">?</a></sup>:</span>
            <span class="sp-metric-value" data-type="iptm"></span></li>
        </ul>
      </div>
      <div class="sp-color-options" data-scheme="structure">
        <strong>Structure color scheme:</strong>
        <div>
          <label class="sp-centered-label">
            <input type="radio" name="sp-scheme" value="subunit" checked>
            by subunit
          </label>
        </div>
        <div>
          <label class="sp-centered-label">
            <input type="radio" name="sp-scheme" value="confidence">
            model confidence (pLDDT)
          </label>
        </div>
        <div class="sp-confidence-legend hidden">
          <div class="sp-centered-label sp-legend-label">
            <span class="sp-color-square" style="background-color: #0053D6"></span>
            Very high (pLDDT > 90)
          </div>
          <div class="sp-centered-label sp-legend-label">
            <span class="sp-color-square" style="background-color: #64CBF3"></span>
            Confident (90 > pLDDT > 70)
          </div>
          <div class="sp-centered-label sp-legend-label">
            <span class="sp-color-square" style="background-color: #FFDB12"></span>
            Low (70 > pLDDT > 50)
          </div>
          <div class="sp-centered-label sp-legend-label">
            <span class="sp-color-square" style="background-color: #FF7D45"></span>
            Very low (pLDDT < 50)
          </div>
        </div>
      </div>
       <div class="sp-color-options hidden" data-scheme="crosslinks">
        <strong>Crosslink color scheme:</strong>
        <div>
          <label class="sp-centered-label">
            <input type="radio" name="crosslink-scheme"
                   value="restraint" checked>

            <span class="sp-color-marker" style="background-color: red">
            clashes
          </span>

          </label>
        </div>

        <div>
          <label class="sp-centered-label">
            <input type="radio" name="crosslink-scheme" value="">
            hide all crosslinks
          </label>
        </div>
        <p class="sp-restraint-note hidden">
          <small>
            <strong>Note:</strong>
            any atom within a residue that is within a 2.4Å distance to another atom on a residue from a different chain is considered a clash violation.
          </small>
        </p>
      </div>
      <div>
        <a class="sp-crosslinks-download"
           href="" download>
          <img src="{{@img/bootstrap-icons/download.svg}}"
               title="Download complex data">
          <span>
          Download structure, crosslink data and PyMOL/ChimeraX files
        </span>
        </a>
      </div>
    </details>
  </div>

</template>
