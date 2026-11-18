"""Hide the Supabase lead forms behind window.DP_FORMS (set in index.html).

When DP_FORMS !== true, every form (footer + /agro, /biznes, /tsl) is replaced
with large phone / e-mail cards. Run once on the original Lovable bundle.
"""
import sys, glob
p = glob.glob('assets/index-*.js')[0]
s = open(p, encoding='utf-8').read()
assert 'function DPC(' not in s, 'already patched'

ON = 'window.DP_FORMS===true'
card = 'flex items-center gap-5 p-6 rounded-xl border border-gold/30 bg-gold/5 hover:bg-gold/10 hover:border-gold transition-all text-left'
icon = 'w-14 h-14 rounded-full bg-gold text-navy flex items-center justify-center flex-shrink-0'
label = 'block text-ivory/50 font-body text-xs uppercase tracking-wider mb-1'
cards = (
 f'a.jsxs("a",{{href:"tel:+48507111122",className:"{card}",children:[a.jsx("span",{{className:"{icon}",children:a.jsx(jn,{{className:"w-6 h-6"}})}}),a.jsxs("span",{{className:"block min-w-0",children:[a.jsx("span",{{className:"{label}",children:"Zadzwoń"}}),a.jsx("span",{{className:"block font-display text-2xl md:text-3xl font-bold text-ivory",children:"507 11 11 22"}})]}})]}}),'
 f'a.jsxs("a",{{href:"mailto:kancelaria@dobryprawnik.eu",className:"{card}",children:[a.jsx("span",{{className:"{icon}",children:a.jsx(f_,{{className:"w-6 h-6"}})}}),a.jsxs("span",{{className:"block min-w-0",children:[a.jsx("span",{{className:"{label}",children:"Napisz e-mail"}}),a.jsx("span",{{className:"block font-display text-xl md:text-2xl font-bold text-ivory",style:{{overflowWrap:"anywhere"}},children:"kancelaria@dobryprawnik.eu"}})]}})]}})'
)
helpers = (
 'function DPC(){return a.jsx("div",{className:"relative max-w-3xl mx-auto grid md:grid-cols-2 gap-4",children:[' + cards + ']})}'
 'function DPF(){return a.jsxs("div",{children:[a.jsx("h2",{className:"font-display text-2xl md:text-3xl font-bold text-gold mb-2",children:"Skontaktuj się z nami"}),'
 'a.jsx("p",{className:"text-ivory/60 font-body leading-relaxed mb-8",children:"Zadzwoń lub napisz – chętnie odpowiemy na Twoje pytania."}),'
 'a.jsxs("div",{className:"space-y-4",children:[' + cards + ']})]})}'
)
# helpers: top-level, hoisted, next to the footer component
assert s.count('function WP(') == 1
s = s.replace('function WP(', helpers + 'function WP(')

# footer: small links only with forms on; form column -> DPF() when off
links = 'a.jsxs("div",{className:"space-y-3",children:[a.jsxs("a",{href:"tel:+48507111122"'
assert s.count(links) == 1
s = s.replace(links, f'{ON}&&' + links)
ff = '!e&&a.jsxs("div",{children:[a.jsx("h2",{className:"font-display text-2xl md:text-3xl font-bold text-gold mb-8",children:"Napisz do nas"})'
assert s.count(ff) == 1
s = s.replace(ff, f'!e&&!({ON})&&DPF(),!e&&{ON}&&a.jsxs("div",{{children:[a.jsx("h2",{{className:"font-display text-2xl md:text-3xl font-bold text-gold mb-8",children:"Napisz do nas"}})')

# subpages: before the success/form ternary
sub = 't?a.jsxs("div",{className:"text-center py-6'
assert s.count(sub) == 3, s.count(sub)
s = s.replace(sub, f'!({ON})?DPC():' + sub)
open(p, 'w', encoding='utf-8').write(s)
print('patched', p)
