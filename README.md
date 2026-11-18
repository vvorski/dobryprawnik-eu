# dobryprawnik.eu

Strona https://dobryprawnik.eu – statyczna kopia https://dobry-prawnik-eu.lovable.app/ hostowana na GitHub Pages.

Kontakt/formularz korzysta z Supabase (bez zmian).

## Ścieżka bazowa

Strona działa pod `https://vvorski.github.io/dobryprawnik-eu/`, dlatego w `index.html`,
`404.html` i `assets/index-*.js` ścieżki mają prefiks `/dobryprawnik-eu`.

Po podpięciu własnej domeny (plik `CNAME` + DNS) usuń prefiks:

```bash
./set-base.sh /
```

## Formularze kontaktowe (wyłączone)

Formularze (stopka „Napisz do nas” oraz /agro, /biznes, /tsl) wysyłały dane do projektu
Supabase z Lovable, który już nie istnieje. Są ukryte, a w ich miejscu wyświetlane są
telefon i e-mail. Kod formularzy jest zachowany.

Aby je włączyć z powrotem (po podłączeniu działającego backendu), w `index.html` i `404.html`
zmień `window.DP_FORMS=false` na `window.DP_FORMS=true`.

Łatka: `tools/patch-forms.py` (uruchamiana raz na oryginalnym bundlu z Lovable).
