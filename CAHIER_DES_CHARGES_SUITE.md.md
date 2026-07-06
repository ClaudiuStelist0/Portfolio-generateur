# Cahier des charges — 4 sites restants (Photographe, Avocat, Artisan, Airbnb)

Ce document permet à n'importe quel outil (Qoder, Cursor, Windsurf, ou une autre
conversation avec Claude) de terminer le projet **exactement dans le même style**
que les 4 sites déjà livrés : restaurant, plombier, coiffeur, coach.

## Où en est le projet

Déjà terminés (dans `portfolio/`) :
- `restaurant/index.html` — noir / blanc / doré
- `plombier/index.html` — bleu / blanc, urgence 24/7
- `coiffeur/index.html` — beige / noir / or, premium
- `coach/index.html` — rouge / noir, dynamique

Encore à faire :
- `photographe/index.html` — blanc / gris / noir, minimaliste
- `avocat/index.html` — bleu marine / doré, institutionnel
- `artisan/index.html` — bois / orange, chaleureux (menuisier)
- `airbnb/index.html` — blanc / rouge corail, inspiré Airbnb
- `index.html` (racine) — page portfolio qui liste les 8 démos

## Comment ça marche techniquement

Tout le design repose sur **un seul système partagé** :
- `assets/site.css` — toute la structure et les composants (héros, cartes,
  galerie, formulaire de contact, footer, menu burger…)
- `assets/site.js` — menu mobile + animation d'apparition au scroll + faux
  envoi du formulaire de contact
- Chaque site est un fichier `index.html` unique qui définit ses propres
  couleurs via des variables CSS (`--bg`, `--accent`, `--text`…) puis réutilise
  les mêmes classes (`.hero`, `.card`, `.gallery`, `.contact-grid`…).

Un générateur Python (`_generator_build.py` + `_generator_sites.py`) a servi à
produire les 4 sites déjà faits. **Tu n'es pas obligé de l'utiliser** : tu peux
aussi copier un `index.html` existant (ex. `restaurant/index.html`) et
remplacer directement le texte et les couleurs à la main — c'est plus simple à
donner à un autre outil qui ne connaît pas le générateur Python.

### Méthode recommandée pour un autre outil IA

Donne-lui cette instruction :

> "Voici un site de démonstration déjà terminé : `restaurant/index.html`
> (utilise `assets/site.css` et `assets/site.js`). Crée un nouveau fichier
> `photographe/index.html` en copiant exactement la même structure HTML
> (header, hero, à propos, services, galerie, contact, footer) mais avec :
> - une palette blanc / gris / noir définie dans les variables CSS `:root`
> - un contenu adapté à un photographe professionnel (portfolio, prestations
>   mariage/portrait/entreprise, galerie de photos)
> - un style minimaliste : moins d'éléments, plus d'espace blanc."

## Palette et contenu pour chacun des 4 sites restants

### 📸 Photographe — "Instant Pur"
- Couleurs : fond blanc `#ffffff`, texte quasi-noir `#171717`, accent gris
  foncé `#2b2b2b`, surface `#f4f4f4`
- Police display : une serif fine (ex. "Fraunces" ou "Playfair Display"),
  corps en "Inter"
- Style : minimaliste, beaucoup de blanc, grandes photos plein cadre
- Contenu : présentation du photographe, 3 prestations (mariage, portrait,
  corporate), galerie de 8 photos, formulaire de contact + carte

### ⚖️ Avocat — "Cabinet Berthier & Associés"
- Couleurs : fond blanc cassé `#f7f8fa`, bleu marine `#0d1b3d` (texte/accent),
  doré `#b8935a` en touche secondaire
- Police display : serif institutionnelle (ex. "Playfair Display" ou "Lora")
- Style : sobre, rassurant, aucune animation flashy
- Contenu : domaines de compétence (droit des affaires, droit immobilier,
  droit de la famille), présentation du cabinet et des avocats, avis clients,
  formulaire de contact confidentiel + carte

### 🪚 Artisan — "L'Établi" (menuisier)
- Couleurs : tons bois `#6b4a33` / crème `#f5efe4`, accent orange `#e07a3f`
- Police display : une slab-serif ou une sans-serif costaude (ex. "Fraunces"
  ou "Poppins")
- Style : chaleureux, texture bois, mise en avant du savoir-faire
- Contenu : présentation de l'artisan, 3 prestations (agencement sur-mesure,
  pose de parquet, mobilier), galerie de réalisations avant/après, formulaire
  de devis + carte

### 🏡 Airbnb — "Villa Belvédère"
- Couleurs : blanc `#ffffff`, texte gris foncé `#222222`, accent rouge
  corail `#ff5a5f` (couleur historique Airbnb)
- Police display : sans-serif arrondie (ex. "Poppins" ou "Nunito")
- Style : inspiré Airbnb — grandes photos, liste d'équipements avec icônes,
  encart prix/nuit, calendrier fictif de disponibilité
- Contenu : présentation du logement, équipements (Wi-Fi, cuisine équipée,
  parking, piscine…), galerie de 8 photos, avis voyageurs, formulaire de
  demande de réservation + carte

## Page portfolio principale (`index.html` à la racine)

Doit lister les 8 démos sous forme de cartes (capture d'écran, nom du métier,
bouton "Voir la démo" pointant vers `restaurant/index.html`,
`plombier/index.html`, etc.), avec une présentation de l'activité de création
de sites (toi) en haut de page, un formulaire de contact, et un footer.

## Important — pas de clé API à protéger

Aucun de ces 8 sites n'utilise de clé API ou de service payant :
- Les images viennent de `picsum.photos` (service gratuit, pas de clé).
- La carte utilise l'iframe Google Maps gratuite (`google.com/maps?q=...&output=embed`),
  pas l'API Google Maps (qui nécessiterait une clé).
- Le formulaire de contact est une simulation en JavaScript (pas d'envoi réel).

Si un jour tu veux un vrai envoi d'e-mail depuis le formulaire, utilise un
service comme **Formspree** ou **EmailJS** : ils fournissent une clé
"publique" (faite pour être visible dans le code, ce n'est pas un secret) —
donc rien à cacher, il suffit de suivre leur documentation pour remplacer le
`<form class="contact-form">` par leur code d'intégration.
