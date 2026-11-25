import { mathjax } from 'mathjax-full/js/mathjax.js';
import { TeX } from 'mathjax-full/js/input/tex.js';
import { SVG } from 'mathjax-full/js/output/svg.js';
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js';
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js';
import fs from 'node:fs';

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({ packages: AllPackages });
const svg = new SVG({ fontCache: 'none' });
const html = mathjax.document('', { InputJax: tex, OutputJax: svg });

const inputRaw = fs.readFileSync(0, 'utf8');
const payload = JSON.parse(inputRaw);
const items = Array.isArray(payload) ? payload : [payload];

const results = items.map(({ latex, display = true }) => {
  const node = html.convert(latex, { display });
  const svgEl = adaptor.firstChild(node);
  let markup = adaptor.outerHTML(svgEl);
  markup = markup.replaceAll('currentColor', '#FFFFFF');
  return markup;
});

process.stdout.write(JSON.stringify(Array.isArray(payload) ? results : results[0]));
