# dobryprawnik.eu

Statyczna kopia strony https://dobry-prawnik-eu.lovable.app/ hostowana na GitHub Pages.

Kontakt/formularz korzysta z Supabase (bez zmian).

## Ścieżka bazowa

Strona działa pod `https://vvorski.github.io/dobryprawnik-eu/`, dlatego w `index.html`,
`404.html` i `assets/index-*.js` ścieżki mają prefiks `/dobryprawnik-eu`.

Po podpięciu własnej domeny (plik `CNAME` + DNS) usuń prefiks:

```bash
./set-base.sh /
```
