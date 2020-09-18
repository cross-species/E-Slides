import { transform } from 'markmap-lib/dist/transform';

const data = transform(markdown);

import { Markmap } from 'markmap-lib/dist/view';

Markmap.create('#markmap', null, data);

// or pass an SVG element directly
const svgEl = document.querySelector('#markmap');
Markmap.create(svgEl, null, data);