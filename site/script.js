// Search, tag filters, a random tip button and "On this day". Without
// JavaScript the page still lists every tip; the controls stay hidden.
// Filters are kept in the URL (?tag=git&q=rebase) so a filtered view can be
// shared, and a tip's own link is its date (#2026-10-23).

const tips = Array.from(document.querySelectorAll('article.tip'));
const text = new Map(tips.map(tip => [tip, tip.textContent.toLowerCase()]));
const controls = document.getElementById('controls');
const chips = Array.from(controls.querySelectorAll('button.tag'));
const search = document.getElementById('search');
const count = document.getElementById('count');
const clear = document.getElementById('clear');
let tag = '';

function apply() {
  const terms = search.value.toLowerCase().split(/\s+/).filter(Boolean);
  let shown = 0;
  for (const tip of tips) {
    const match = (!tag || tip.dataset.tags.split(' ').includes(tag)) &&
      terms.every(term => text.get(tip).includes(term));
    tip.hidden = !match;
    if (match) shown++;
  }
  for (const chip of chips) {
    chip.setAttribute('aria-pressed', String(chip.dataset.tag === tag));
    if (chip.dataset.tag === tag && chip.closest('details')) chip.closest('details').open = true;
  }
  const filtered = Boolean(tag || terms.length);
  count.textContent = filtered ? `${shown} of ${tips.length} tips` : `${tips.length} tips`;
  clear.hidden = !filtered;
}

// Save the filters in the URL. A filter change drops the tip link (#date)
// unless the caller passes it back.
function remember(hash = '') {
  const params = new URLSearchParams();
  if (tag) params.set('tag', tag);
  if (search.value.trim()) params.set('q', search.value.trim());
  const query = params.toString();
  history.replaceState(null, '', (query ? `?${query}` : location.pathname) + hash);
}

// Scroll to the tip in the URL, clearing the filters if they hide it.
function reveal() {
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (!target || !target.matches('article.tip')) return;
  if (target.hidden) {
    tag = '';
    search.value = '';
    apply();
    remember(location.hash);
  }
  target.scrollIntoView();
}

function onThisDay() {
  const now = new Date();
  const monthDay = `-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
  const year = String(now.getFullYear());
  const list = document.querySelector('#on-this-day ul');
  for (const tip of tips) {
    if (!tip.id.endsWith(monthDay) || tip.id.startsWith(year)) continue;
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = `#${tip.id}`;
    link.textContent = tip.id.slice(0, 4);
    const words = document.createElement('span');
    words.append(...Array.from(tip.querySelector('h2').childNodes, node => node.cloneNode(true)));
    item.append(link, words);
    list.append(item);
  }
  list.parentElement.hidden = !list.children.length;
}

document.addEventListener('click', event => {
  const button = event.target.closest('button.tag');
  if (!button) return;
  tag = button.dataset.tag === tag ? '' : button.dataset.tag;
  apply();
  remember();
  if (!controls.contains(button)) controls.scrollIntoView();
});

search.addEventListener('input', () => {
  apply();
  remember();
});

clear.addEventListener('click', () => {
  tag = '';
  search.value = '';
  apply();
  remember();
  search.focus();
});

document.getElementById('random').addEventListener('click', () => {
  const pool = tips.filter(tip => !tip.hidden && `#${tip.id}` !== location.hash);
  if (pool.length) location.hash = pool[Math.floor(Math.random() * pool.length)].id;
});

window.addEventListener('hashchange', reveal);

const params = new URLSearchParams(location.search);
if (chips.some(chip => chip.dataset.tag === params.get('tag'))) tag = params.get('tag');
search.value = params.get('q') || '';
apply();
onThisDay();
controls.hidden = false;
reveal();
