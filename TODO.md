# TODO — Site ScarCity (storytellise.com)

Dernière mise à jour : 16 nov. 2026 (soir)
Pages concernées : `index.html` (EN), `scarcity-fr.html` (FR), `cover.jpg`
Animation : `cascade-flow-20.gif` / `.mp4` — **VERSION FINALE VERROUILLÉE** (flow-20 = flow-16 + barquettes hautes figées, barquette du bas intacte, base flow-13 : ciel statique + feuilles préférées)

## 📅 17 nov. (fait)

- [x] **Versions Instagram** : carré 1:1 → `cascade-flow-20-instagram-feed.mp4` (recadré cascade, 2,1 Mo) ✅
- [x] **Story 9:16** : `cascade-flow-20-story-tiktok.mp4` (recadré cascade, 2,6 Mo) ✅
- [x] **TikTok 9:16** : même fichier que la Story (formats identiques) ✅ — l'utilisateur n'a pas encore de compte TikTok, fichier prêt pour plus tard
- [x] Netteté 800 px validée comme suffisante (compression des plateformes + unsharp mask)
- [x] Pipeline sauvegardé dans `animation/` (scripts + traces + 56 trames, 37 Mo)

## 17 nov. (suite) — bannière animée + header Hugh Howey + Instagram

- [x] **Bannière animée** en haut des pages principales : `cascade-flow-20-banner.mp4` (1600×1062, 1,6 Mo) + poster JPEG (271 Ko), autoplay muted loop, `object-fit: cover`, dégradé vers le fond, `prefers-reduced-motion` respecté (poster statique). Surimpression testée : **slogan en haut (« Bonheur. Santé. Vie privée. / Choisissez-en deux. ») + ScarCity en gros dessous** + ligne auteur. Héros sous-jacent ajusté (slogan-box et doublon du titre retirés).
- [x] **Header 3 zones** (façon hughhowey.com) sur les 4 pages : onglets à gauche (ScarCity · Bio · switch langue), **E.F. Wick centré** (masqué sur mobile), contacts/réseaux à droite.
- [x] **Instagram** (@storytellise) : icône SVG dans le header (droite) + lien texte dans le footer, sur les 4 pages.
- [x] **Bannière VALIDÉE** : fond = peinture entière (version recadrée cascade testée puis écartée), texte = **ScarCity en gros puis slogan dessous** (pas de sous-titre), contraste renforcé (voile radial + ombres nettes). Fichiers : `cascade-flow-20-banner.mp4/.jpg` (utilisé) et `-cascade.mp4/.jpg` (archivé).

## 17 nov. — fiche, saga, bio (fait)

- [x] **Fiche du livre** complétée depuis Amazon.fr / Kobo / Amazon.it : parution **31 mai 2026**, broché **370 p.** (FR) / **386 p.** (EN) · **478 p.** ebook, **ISBN 979-1098083105**, **13,95 € TTC** broché FR / **$14.99** EN · **3,49 €** ebook FR / **$3.99** EN (mêmes prix toutes plateformes), note **5/5 (2 avis Amazon.fr)**. Grille passée en 3×2 tuiles sur les deux pages (FR + EN). Pages actualisées en conséquence.
- [x] **Saga / Tome 2** : en cours d'écriture, **à paraître automne 2027** — cartes mises à jour (badge « En écriture », titre « Automne 2027 », CTA « Me prévenir »). Option plus prudente proposée à l'utilisateur (date à ajuster s'il préfère).
- [x] **Bio auteur** : bios complètes intégrées (fichiers ODT ProtonDrive fournis par l'utilisateur) — **pages dédiées `auteur.html` / `author.html`** créées dans le design du site (6 paragraphes, citation « Satisfaction garantie » en exergue, retour ScarCity, switch FR/EN, animations reveal) + **teaser + lien** sur les pages principales. Vérifié au navigateur (FR + EN) : titres, lang, paragraphes, liens ✓.

## 🔲 Suite : contenu du site (attendu de l'utilisateur)

## ✅ Terminé (16 nov.)

- [x] Site FR/EN : toutes les corrections techniques + sections (voir SESSION-LOG.md)
- [x] Animation aquarelle complète : cascade, mer, 2 serpenteins (rouge/noir), feuilles qui coulent, silhouettes, fumée, scintillement — 20 versions archivées sans écrasement
- [x] Formats : GIF 800px (2,7 Mo) + MP4 720×478 (450 Ko)

## 🔲 En attente de contenu (site)

- [x] **Citation choc** : « Pour votre sécurité, marchez, bougez, rechargez. Conservez énergie et santé. » (fournie par l'utilisateur) — remplace « Satisfaction garantie* » dans la quote-band FR + traduction EN (« For your safety: walk, move, recharge. Preserve energy and health. ») ✅
- [x] **Bug page noire extrait corrigé** : la section lecture (5 000 px de haut) n'atteignait jamais le seuil de 12 % de l'IntersectionObserver → classe `reveal` retirée des pages extrait/excerpt (opacité désormais 1, vérifié).
- [x] **Avis lecteurs (FR)** : ligne ★★★★★ 5/5 · 2 avis Amazon.fr sous les boutons d'achat (page FR), lien vers la fiche Amazon. EN : en attente de savoir si l'édition anglaise a des avis.
- [ ] **Newsletter** — lien d'inscription réel (Substack, Mailchimp…)
- [x] **Extrait** : pages dédiées **`extrait.html`** (FR, 87 §) / **`excerpt.html`** (EN, 85 §) — « La Redirection » / « The Redirection », typographie lecture (1,13 rem, interligne 1,9, lettrine dorée, texte justifié), titre + date du chapitre, fondu de fin + CTA « Lire la suite — Acheter sur Amazon ». **Aucune mention de « chapitre 1 »** (anti-spoil). Onglet « Extrait/Excerpt » dans la nav des 6 pages + **teaser sur les accueil** (« Lisez les premières pages » + bouton). Vérifié au navigateur.
- [x] **Goodreads** — fiches réelles : **FR** https://www.goodreads.com/book/show/252914907 (ebook) sur la page FR, **EN** https://www.goodreads.com/book/show/262723184 (ebook) sur la page EN ✅
- [x] **RGPD + mentions légales** : `mentions.html` créée (éditeur, hébergement GitHub Pages, propriété intellectuelle, RGPD, liens externes), **bandeau cookies** sur les 6 pages (Accepter/Refuser, choix mémorisé), **Google Analytics chargé uniquement après consentement** (localStorage), liens footer.
- [x] **Newsletter (popup)** : popup bas-droite sur les 6 pages (« Nouvelles de l'HemiNor »), apparition après 14 s ou 40 % de scroll (1 fois/7 j, mémorisé), formulaire email + bouton. **Fallback mailto actif** ; point de branchement `NL_ENDPOINT` (1 variable) pour un service tiers (Buttondown/Formspree/Mailchimp/Brevo) — à choisir avec l'utilisateur.
- [x] **Extrait — VÉRIFIÉ MOT À MOT** : diff automatisé ODT↔page = **0 différence** (FR 2 871 mots, EN 2 870 mots). Corps commence à « Les sept Terminaux… », date en sous-titre grisé uniquement. Typographie : italiques sources préservées, indentations fidèles (tabulations ODT), interligne simple, 2 Messpam encadrés blancs pleine largeur, annonces intercom en italique doré. Seule liberté typographique : guillemets français « » pour l'annonce (l'ODT a des “ ”).
- [ ] **Newsletter** — lien d'inscription réel
- [ ] **Extrait chapitre 1** — texte → section dédiée
- [ ] **Lien Goodreads** — fiche réelle du livre
- [ ] RGPD (bandeau cookies), mentions légales, réseaux sociaux, formats papier/audio
