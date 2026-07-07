# Portfolio de démonstration — 8 sites vitrines

## État d'avancement

✅ Terminés : Tous les 8 sites sont maintenant complets !
- `restaurant/` — Restaurant gastronomique
- `plombier/` — Plombier professionnel
- `coiffeur/` — Salon de coiffure premium
- `coach/` — Coach sportif
- `photographe/` — Photographe professionnel
- `avocat/` — Cabinet d'avocats
- `artisan/` — Menuisier artisan
- `airbnb/` — Location de vacances
- `index.html` — Page d'accueil du portfolio

Voir **`CAHIER_DES_CHARGES_SUITE.md`** pour le détail complet permettant de
terminer les 4 sites restants avec n'importe quel outil, en gardant exactement
le même style.

## Comment héberger sur GitHub Pages (gratuit)

1. Crée un dépôt GitHub, par exemple `portfolio`.
2. Mets tout le contenu de ce dossier (`restaurant/`, `plombier/`, `assets/`…)
   à la racine du dépôt.
3. Dans le dépôt GitHub : **Settings → Pages → Source → Deploy from a branch**,
   choisis la branche `main` et le dossier `/ (root)`.
4. Après 1 à 2 minutes, ton portfolio est en ligne à l'adresse :
   `https://ton-pseudo.github.io/portfolio/`
5. Chaque site est accessible via, par exemple :
   `https://ton-pseudo.github.io/portfolio/restaurant/`

Aucune installation, aucun build, aucune clé à configurer : ce sont des
fichiers HTML/CSS/JS statiques, prêts à être servis tels quels.

## Aucune clé API à protéger

Voir la fin de `CAHIER_DES_CHARGES_SUITE.md` — ces sites n'utilisent aucune
clé API (images via picsum.photos, carte via l'iframe Google Maps gratuite,
formulaire de contact simulé en JavaScript).

## Pour ajouter un vrai envoi d'e-mail

Si vous souhaitez remplacer le formulaire de démonstration par un vrai système d'envoi d'e-mail, vous pouvez utiliser :

### Option 1: Formspree
1. Remplacez l'attribut `action` du formulaire par `https://formspree.io/f/votre-id`
2. Ajoutez un champ caché avec votre adresse e-mail
3. Aucune configuration serveur nécessaire

### Option 2: EmailJS
1. Inscrire-vous sur [EmailJS](https://www.emailjs.com/)
2. Ajoutez le script EmailJS dans votre `<head>`
3. Configurez le service e-mail et le template
4. Remplacez la fonction JavaScript de soumission du formulaire

Exemple de configuration EmailJS :
```html
<script src="https://cdn.jsdelivr.net/npm/emailjs-com@3/dist/email.min.js"></script>
<script>
  emailjs.init('votre-user-id');
</script>
```

## Liste complète des sites

Le portfolio contient maintenant 8 sites vitrines complets :

1. **Restaurant** — Cuisine gastronomique à Lyon
2. **Plombier** — Dépannage et services techniques
3. **Coiffeur** — Salon premium avec rendez-vous en ligne
4. **Coach** — Programmes d'accompagnement sportif
5. **Photographe** — Prestations mariage, portrait et corporate
6. **Avocat** — Cabinet juridique spécialisé
7. **Artisan** — Menuiserie et agencement sur-mesure
8. **Airbnb** — Location de vacances avec piscine

Chaque site utilise le même système technique mais avec une identité visuelle unique.

## Fichiers techniques (à ignorer si tu ne codes pas en Python)

`_generator_build.py` et `_generator_sites.py` sont les scripts qui ont servi
à générer les 4 sites terminés. Ils ne sont pas nécessaires pour héberger le
site — tu peux les supprimer du dépôt GitHub si tu veux, ou les garder pour
générer les 4 sites restants si tu relances une session avec moi.
