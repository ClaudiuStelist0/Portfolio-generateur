import sys
sys.path.insert(0, "/home/claude")
from build import page, hero, apropos, services, gallery_section, testimonials_section, banner_section, contact_section

# =========================================================
# 1. RESTAURANT — "Le Cerisier" — noir / blanc / doré
# =========================================================
page(
    "restaurant/index.html",
    title="Le Cerisier — Restaurant gastronomique à Lyon",
    meta_desc="Restaurant gastronomique Le Cerisier à Lyon. Cuisine de saison, cadre élégant, réservation en ligne.",
    font_display_url="Playfair+Display:wght@600;700", font_display="Playfair Display",
    font_body_url="Inter:wght@400;500;600", font_body="Inter",
    bg="#0e0d0c", surface="#161514", text="#f3efe8", muted="#a89f8f",
    line="#2a2724", line_strong="#3a3632",
    accent="#c9a24a", accent_contrast="#0e0d0c", radius="4px",
    extra_css=".hero-media{border:1px solid #2a2724;}",
    brand_name="Le", brand_suffix="Cerisier",
    services_label="Menu",
    nav_cta="Réserver une table",
    hero=hero(
        eyebrow="Restaurant gastronomique — Lyon",
        title="Une cuisine de saison, servie avec caractère.",
        lede="Le Cerisier propose une cuisine française contemporaine, construite autour de produits locaux et d'une carte qui change au rythme des saisons.",
        cta_primary="Réserver une table",
        cta_ghost="Découvrir le menu",
        img_seed="cerisier-hero", img_ratio="4/5",
        stats=[("12", "ans d'existence"), ("4.8/5", "note moyenne"), ("38", "places assises")],
    ),
    apropos=apropos(
        eyebrow="À propos",
        title="L'histoire d'une table lyonnaise",
        paragraphs=[
            "Ouvert en 2014 dans le quartier de la Croix-Rousse, Le Cerisier est né de l'envie de proposer une cuisine exigeante dans un cadre sobre et chaleureux.",
            "Le chef travaille en direct avec des producteurs de la région pour composer une carte courte, renouvelée toutes les trois semaines selon les arrivages.",
            "La salle, habillée de bois sombre et de touches dorées, accueille 38 couverts autour d'une cuisine ouverte.",
        ],
        img_seed="cerisier-chef",
    ),
    services=services(
        eyebrow="La carte",
        title="Ce que nous proposons",
        lede="Un menu resserré, pensé pour mettre en valeur chaque produit de saison.",
        items=[
            ("🍷", "Menu dégustation", "5 services accordés avec une sélection de vins nature, sur réservation."),
            ("🍽️", "Carte du soir", "Une carte courte renouvelée toutes les 3 semaines selon les saisons."),
            ("🥂", "Privatisation", "La salle ou le salon privé pour vos événements jusqu'à 24 personnes."),
        ],
    ),
    extra_section=gallery_section(
        eyebrow="Galerie",
        title="La salle et les assiettes",
        seeds=["cerisier-1","cerisier-2","cerisier-3","cerisier-4","cerisier-5","cerisier-6","cerisier-7","cerisier-8"],
    ) + testimonials_section(
        eyebrow="Avis clients",
        title="Ce qu'en disent nos habitués",
        quotes=[
            ("Une carte courte mais d'une précision rare. Le service est attentif sans être intrusif.", "Camille R.", "Cliente régulière"),
            ("Le menu dégustation vaut le déplacement depuis Paris. Accord mets-vins impeccable.", "Julien M.", "Guide gastronomique"),
            ("Cadre élégant, cuisine généreuse. Notre restaurant préféré pour les grandes occasions.", "Sophie & Marc", "Clients depuis 2018"),
        ],
        alt=False,
    ),
    contact=contact_section(
        eyebrow="Réservation",
        title="Réserver une table",
        lede="Par téléphone, par e-mail ou via le formulaire ci-dessous — nous confirmons sous 24h.",
        phone="04 78 00 00 00", email="contact@le-cerisier-demo.fr",
        address="14 rue des Tables Claudiennes, 69001 Lyon", hours="Mar–Sam · 12h–14h / 19h30–22h30",
        map_query="Croix-Rousse+Lyon", submit_label="Envoyer la demande de réservation",
    ),
    footer_tagline="Cuisine de saison et cadre élégant au cœur de Lyon.",
    phone="04 78 00 00 00", email="contact@le-cerisier-demo.fr", address="Croix-Rousse, Lyon",
)
print("Restaurant OK")

# =========================================================
# 2. PLOMBIER — "AquaFix" — bleu / blanc — urgence 24/7
# =========================================================
page(
    "plombier/index.html",
    title="AquaFix — Plombier à Marseille, dépannage 24/7",
    meta_desc="AquaFix, plombier professionnel à Marseille. Dépannage urgent 24h/24, devis gratuit, intervention rapide.",
    font_display_url="Poppins:wght@600;700", font_display="Poppins",
    font_body_url="Inter:wght@400;500;600", font_body="Inter",
    bg="#ffffff", surface="#f2f6fb", text="#0f2136", muted="#5b6c80",
    line="#dfe7ef", line_strong="#c3d3e2",
    accent="#1466d1", accent_contrast="#ffffff", radius="8px",
    extra_css="",
    brand_name="Aqua", brand_suffix="Fix",
    services_label="Services",
    nav_cta="Devis gratuit",
    hero=hero(
        eyebrow="Plombier professionnel — Marseille et alentours",
        title="Une fuite ? On est chez vous en moins d'une heure.",
        lede="AquaFix intervient 7j/7 pour tous vos travaux de plomberie : dépannage d'urgence, installation sanitaire et rénovation de salle de bain.",
        cta_primary="Demander un devis gratuit",
        cta_ghost="Voir nos services",
        img_seed="aquafix-hero", img_ratio="4/5",
        badge="🔧 Urgence 24h/24 — 7j/7",
        stats=[("15", "ans d'expérience"), ("2 400+", "interventions"), ("45 min", "délai moyen")],
    ),
    apropos=apropos(
        eyebrow="À propos",
        title="Une équipe de plombiers certifiés",
        paragraphs=[
            "AquaFix est une entreprise familiale fondée en 2009, spécialisée dans le dépannage d'urgence et l'installation sanitaire pour les particuliers et les copropriétés.",
            "Nos plombiers sont certifiés RGE et interviennent avec des véhicules équipés pour traiter la majorité des pannes dès le premier passage.",
            "Nous appliquons systématiquement un devis gratuit avant toute intervention non urgente, sans surprise sur la facture.",
        ],
        img_seed="aquafix-team",
    ),
    services=services(
        eyebrow="Nos services",
        title="Une solution pour chaque besoin",
        lede="Du dépannage express à la rénovation complète, une seule équipe pour tout gérer.",
        items=[
            ("🚿", "Dépannage d'urgence", "Fuite, canalisation bouchée, panne de chauffe-eau : intervention rapide 24h/24."),
            ("🛁", "Rénovation sanitaire", "Installation ou remplacement de douche, baignoire, WC et robinetterie."),
            ("🏢", "Copropriétés", "Contrats d'entretien et interventions programmées pour les parties communes."),
        ],
    ),
    extra_section=banner_section(
        title="Une urgence en cours ?",
        text="Notre astreinte répond 24h/24 et 7j/7, week-ends et jours fériés compris.",
        cta="Appeler l'astreinte",
    ) + testimonials_section(
        eyebrow="Avis clients",
        title="La confiance de nos clients",
        quotes=[
            ("Intervention en 40 minutes un dimanche soir pour une fuite sous l'évier. Très professionnel.", "Nadia B.", "Marseille 8e"),
            ("Devis clair, travail soigné pour la rénovation complète de notre salle de bain.", "Thomas L.", "Client particulier"),
            ("Contrat d'entretien pour notre copropriété depuis 3 ans, toujours réactifs.", "Cabinet Immo Sud", "Syndic"),
        ],
    ),
    contact=contact_section(
        eyebrow="Contact",
        title="Demander une intervention",
        lede="Décrivez votre besoin, nous vous rappelons sous 30 minutes en journée.",
        phone="04 91 00 00 00", email="contact@aquafix-demo.fr",
        address="22 avenue du Prado, 13006 Marseille", hours="Astreinte 24h/24 · Bureau : Lun–Ven 8h–19h",
        map_query="Avenue+du+Prado+Marseille", submit_label="Envoyer ma demande",
    ),
    footer_tagline="Dépannage plomberie 24h/24 à Marseille et sa région.",
    phone="04 91 00 00 00", email="contact@aquafix-demo.fr", address="Avenue du Prado, Marseille",
)
print("Plombier OK")

# =========================================================
# 3. COIFFEUR — "Maison Lumière" — beige / noir / or — premium/féminin
# =========================================================
page(
    "coiffeur/index.html",
    title="Maison Lumière — Salon de coiffure premium à Paris",
    meta_desc="Maison Lumière, salon de coiffure premium à Paris. Coupe, coloration, soins. Prise de rendez-vous en ligne.",
    font_display_url="Cormorant+Garamond:wght@600;700", font_display="Cormorant Garamond",
    font_body_url="Jost:wght@400;500;600", font_body="Jost",
    bg="#faf6f0", surface="#f1e9dc", text="#241f18", muted="#7a6f5d",
    line="#e6dbc7", line_strong="#d8c9ac",
    accent="#b08d3f", accent_contrast="#faf6f0", radius="2px",
    extra_css=".hero h1{font-weight:600;} .eyebrow{color:#8a6d2f;}",
    brand_name="Maison", brand_suffix="Lumière",
    services_label="Prestations",
    nav_cta="Prendre rendez-vous",
    hero=hero(
        eyebrow="Salon de coiffure premium — Paris 8e",
        title="Une lumière qui révèle chaque chevelure.",
        lede="Maison Lumière est un salon confidentiel dédié à la coupe, la coloration et aux soins capillaires haut de gamme, dans un cadre pensé pour la détente.",
        cta_primary="Prendre rendez-vous",
        cta_ghost="Découvrir nos prestations",
        img_seed="lumiere-hero", img_ratio="4/5",
        stats=[("9", "coiffeurs experts"), ("4.9/5", "note clientèle"), ("2012", "année d'ouverture")],
    ),
    apropos=apropos(
        eyebrow="À propos",
        title="L'art du geste précis",
        paragraphs=[
            "Fondé en 2012 par Camille Vasseur, Maison Lumière s'est imposé comme une référence parisienne pour la coloration végétale et les coupes sur-mesure.",
            "Chaque prestation débute par un diagnostic capillaire approfondi, pour adapter le geste et les produits à la nature de chaque chevelure.",
            "Le salon travaille exclusivement avec des marques françaises engagées dans une démarche plus respectueuse du cheveu et de l'environnement.",
        ],
        img_seed="lumiere-salon",
        reverse=True,
    ),
    services=services(
        eyebrow="Prestations",
        title="Nos soins signature",
        lede="Des prestations pensées pour sublimer chaque type de cheveu.",
        items=[
            ("✂️", "Coupe sur-mesure", "Diagnostic personnalisé et coupe adaptée à la texture et à la morphologie du visage."),
            ("🎨", "Coloration végétale", "Techniques de balayage et coloration à base de pigments naturels."),
            ("💆", "Rituels soin", "Soins profonds en cabine pour restaurer, hydrater et fortifier la fibre capillaire."),
        ],
    ),
    extra_section=gallery_section(
        eyebrow="Galerie",
        title="Nos réalisations",
        seeds=["lumiere-1","lumiere-2","lumiere-3","lumiere-4","lumiere-5","lumiere-6","lumiere-7","lumiere-8"],
    ),
    contact=contact_section(
        eyebrow="Rendez-vous",
        title="Réserver un créneau",
        lede="Le salon fonctionne uniquement sur rendez-vous, en semaine comme le week-end.",
        phone="01 45 00 00 00", email="rdv@maison-lumiere-demo.fr",
        address="9 rue du Faubourg Saint-Honoré, 75008 Paris", hours="Mar–Sam · 9h30–19h",
        map_query="Faubourg+Saint-Honore+Paris", submit_label="Demander un rendez-vous",
    ),
    footer_tagline="Coupe, coloration et soins premium au cœur de Paris.",
    phone="01 45 00 00 00", email="rdv@maison-lumiere-demo.fr", address="Faubourg Saint-Honoré, Paris",
)
print("Coiffeur OK")


# =========================================================
# 4. COACH SPORTIF — "ForgeFit" — rouge / noir — dynamique
# =========================================================
page(
    "coach/index.html",
    title="ForgeFit — Coaching sportif personnalisé à Bordeaux",
    meta_desc="ForgeFit, coach sportif à Bordeaux. Programmes personnalisés, suivi nutritionnel, coaching en salle ou à domicile.",
    font_display_url="Anton", font_display="Anton",
    font_body_url="Inter:wght@400;500;600;700", font_body="Inter",
    bg="#0c0c0c", surface="#161616", text="#f5f5f5", muted="#9a9a9a",
    line="#262626", line_strong="#3a3a3a",
    accent="#e13030", accent_contrast="#ffffff", radius="4px",
    extra_css=".hero h1{text-transform:uppercase; letter-spacing:.01em;} .section-title{text-transform:uppercase;}",
    brand_name="Forge", brand_suffix="Fit",
    services_label="Programmes",
    nav_cta="Séance d'essai",
    hero=hero(
        eyebrow="Coach sportif certifié — Bordeaux",
        title="Ton corps a un potentiel. On va le forger.",
        lede="Programmes de coaching individuel ou en petit groupe, construits autour de tes objectifs réels : perte de poids, prise de masse ou remise en forme.",
        cta_primary="Réserver une séance d'essai",
        cta_ghost="Voir les programmes",
        img_seed="forgefit-hero", img_ratio="4/5",
        stats=[("300+", "clients accompagnés"), ("7", "ans d'expérience"), ("92%", "d'objectifs atteints")],
    ),
    apropos=apropos(
        eyebrow="À propos",
        title="Un coaching basé sur des résultats mesurables",
        paragraphs=[
            "Diplômé d'État et spécialisé en préparation physique, j'accompagne des particuliers de tous niveaux depuis 2017, en salle comme à domicile.",
            "Chaque programme démarre par un bilan complet (mobilité, composition corporelle, objectifs) pour construire un plan réaliste et évolutif.",
            "Le suivi inclut un point nutrition mensuel et un ajustement du programme toutes les 4 semaines selon la progression.",
        ],
        img_seed="forgefit-coach",
    ),
    services=services(
        eyebrow="Programmes",
        title="Un accompagnement pour chaque objectif",
        lede="Coaching individuel, en duo ou en petit groupe — en salle ou à domicile.",
        items=[
            ("🔥", "Perte de poids", "Programme combinant renforcement, cardio et suivi nutritionnel sur 12 semaines."),
            ("💪", "Prise de masse", "Plan de musculation progressif avec suivi des charges et de la récupération."),
            ("🏃", "Remise en forme", "Reprise du sport en douceur, mobilité et renforcement général."),
        ],
    ),
    extra_section=gallery_section(
        eyebrow="Résultats",
        title="Avant / après",
        seeds=["forgefit-1","forgefit-2","forgefit-3","forgefit-4","forgefit-5","forgefit-6","forgefit-7","forgefit-8"],
    ) + testimonials_section(
        eyebrow="Témoignages",
        title="Ce que disent mes clients",
        quotes=[
            ("12 kilos perdus en 4 mois avec un vrai suivi, pas juste un programme sur papier.", "Karim D.", "Client depuis 2024"),
            ("Le suivi nutrition en plus des séances a tout changé pour moi.", "Élodie F.", "Cliente depuis 2023"),
            ("Programme exigeant mais adapté à mon niveau. Résultats visibles dès le 2e mois.", "Antoine P.", "Client depuis 2025"),
        ],
        alt=False,
    ),
    contact=contact_section(
        eyebrow="Contact",
        title="Réserver ta séance d'essai",
        lede="Premier échange gratuit pour définir tes objectifs et le format le plus adapté.",
        phone="06 00 00 00 00", email="contact@forgefit-demo.fr",
        address="Quartier des Chartrons, 33000 Bordeaux", hours="Lun–Sam · 7h–20h30",
        map_query="Chartrons+Bordeaux", submit_label="Réserver ma séance d'essai",
    ),
    footer_tagline="Coaching sportif individuel à Bordeaux, en salle ou à domicile.",
    phone="06 00 00 00 00", email="contact@forgefit-demo.fr", address="Chartrons, Bordeaux",
)
print("Coach OK")
