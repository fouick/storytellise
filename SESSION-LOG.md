# Journal de session - Site ScarCity (storytellise)

Session du 15 novembre 2026 - assistant OpenCode (GLM-5.3-Flash)
Voir aussi : `TODO.md` pour l'état des tâches.

## Demande 1 - Alignement des headers

> « Aligner les headers "Bonheur, santé, vie privée" avec le titre Scarcity sur la droite »

- **Diagnostic** : `.hero-container` était en `align-items: center` → slogan à y=317, titre ScarCity à y=140 (vérifié au navigateur).
- **Correctif** : `align-items: flex-start` sur desktop + `align-items: stretch` dans la media query mobile (≤ 968 px) pour préserver le rendu mobile.
- **Fichiers** : `index.html`, `scarcity-fr.html`. Résultat : slogan et titre alignés à y=140.

## Demande 2 - Boutons d'achat sous la couverture

> « Mettre les boutons d'achat (en bas à droite) sous l'image de couverture. Rendu plaisant. »

- Déplacement du bloc `.cta-wrapper` (Amazon, Fnac, Kobo, Google Books / Amazon, Google Books, Kobo) de `hero-right` vers `hero-left`, après `.cover-box`.
- La ligne d'accent décorative a suivi, centrée : règle `.hero-left .accent-line { margin: 25px auto 20px auto; }`.
- Évolution du style : d'abord grille 2×2 (`flex: 1 1 calc(50% - 10px)`), puis, à la demande, **une seule ligne** :
  - `.hero-left .cta-wrapper { max-width: 400px; flex-wrap: nowrap; gap: 10px; }` (400 px = largeur de la couverture, mesuré)
  - `.hero-left .btn-action { flex: 1 1 auto; font-size: 0.9rem; padding: 9px 10px; white-space: nowrap; }`
  - `box-sizing: border-box` ajouté sur `.btn-action` ; mobile : `flex: 0 0 auto; width: 100%` en colonne.
- Mobile : `.cta-wrapper { align-items: center }` ajouté.

## Demande 3 - Libellés Amazon

> « Enlève "buy on" et "acheter sur" dans les boutons Amazon »

- `Acheter sur Amazon` → `Amazon` (FR) ; `Buy on Amazon` → `Amazon` (EN).

## Demande 4 - Sous-titre sous ScarCity

> « Supprime "generation silix" sous le titre ; remplace par "Volume 1 of the dystopian saga" (FR : "Le premier tome de ...") »

- `<div class="author-name">` réécrit :
  - EN : « Volume 1 of the dystopian saga by E.F. Wick » → puis, demande suivante : **« The first volume of the dystopian saga by E.F. Wick »**
  - FR : « Le premier tome de la saga dystopique de E.F. Wick »
- E.F. Wick conservé (gras) ; à retirer si demandé.

## Demande 5 - Titre d'onglet

> « Changer le nom de la page dans l'onglet »

- Choix utilisateur : **« ScarCity - E.F. Wick »** (option recommandée) sur les deux pages.

## Demande 6 - Audit « que manque-t-il ? »

Audit livré (voir conversation) : bugs (lang, favicon 404, base64 670 Ko, pas de meta description/OG/JSON-LD, HTML invalide) + manques éditoriaux (avis, bio, fiche technique, extrait, newsletter, Goodreads, RGPD…).

## Demande 7 - « Fais-moi ta plus belle proposition » → implémentation

**Fondations :**
- Couverture extraite du base64 → `cover.jpg` (640×1024, 493 Ko) ; pages 670 Ko → ~13 Ko.
- `<html lang="en">` corrigé sur index.html.
- Favicon SVG inline (S doré sur fond sombre).
- Meta description FR/EN, Open Graph, Twitter Cards (og:image = storytellise.com/cover.jpg).
- Canonical + hreflang (FR ↔ EN, x-default = EN).
- JSON-LD `schema.org/Book` (name, author, inLanguage, genre, bookEdition, workExample EBook + ReadAction vers Amazon).
- HTML valide : `<p class="synopsis-text">` → `<div class="synopsis-text">` (le `<div class="accent-line">` imbriqué était illégal).

**Sections ajoutées (avant `</main>`, style cohérent avec le thème) :**
1. Citation choc (`blockquote.big-quote`) : « Satisfaction garantie* » / « Satisfaction guaranteed* ».
2. Fiche du livre (`.specs-grid`, 4 tuiles) - `id="livre"` / `id="book"` sur le hero.
3. « Pour les lecteurs de… » (`.vibes-grid`) : Divergente/Silo/Black Mirror + bouton Goodreads (lien recherche à remplacer par la vraie fiche).
4. L'auteur (`.author-bio` + monogramme « EW ») - **bio provisoire marquée `<!-- REMPLACEZ -->`**.
5. La saga (`.series-grid`) : Tome 1 Disponible (Amazon) / Tome 2 À venir (`<!-- REMPLACEZ -->`).
6. Newsletter (mailto en attendant un vrai formulaire - `<!-- REMPLACEZ -->`).
- Animations : `.reveal` + IntersectionObserver, seuil 0.12, respect de `prefers-reduced-motion`.
- Responsive : media query mobile enrichie (grilles 1-2 colonnes, bio centrée).

## À demain

L'utilisateur reviendra avec du contenu pour toutes les rubriques (voir `TODO.md`, section « En attente de contenu »).
Notes : domaine confirmé `storytellise.com` (CNAME). Reste à traiter : RGPD/cookies (gtag sans bandeau), mentions légales, liens sociaux, formats paperback/audio.

---

# 16 novembre 2026 - Animation de l'œuvre (cascade-flow.gif)

Source : image aquarelle fournie par l'utilisateur (`/Users/fouick/Desktop/Screens/Elise found this on 2026-11-16 à 13.01.11.png`, 2532×1678 - **droits détenus par l'utilisateur, ne pas partager**).
Outils : Pillow + numpy installés via pip (python3 système).

**`cascade-flow.gif`** (2,4 Mo, 960 px de large, 28 trames = boucle seamless de 2,8 s) :

1. Cascade : flux vertical du filet d'eau (np.roll + fondu), gated chromatique (dest+source) pour ne pas entraîner la falaise
2. Mer : dérive horizontale ondulée par ligne, gated chromatique
3. Écume de la cascade : pulsation lumineuse
4. Écume du rivage : glissement tangent le long de la côte + **rafales de vent vers les barquettes** (direction normale 0,93/-0,37, amplitude 4,8 px)
5. Feuilles blanches : **chute lente vers le fond** - 2 cycles par boucle (sin², amplitude 18 px) + balancement
6. Algues : balancement horizontal réaliste (amplitude décroissante vers le pied), gate « verdâtre »
7. Fumée chaude : nuage rouille/ocre (couleur échantillonnée 164,134,116 de la zone feu, haut-droite) qui s'avance du coin supérieur droit **vers la cascade** (avance/retour doux sur la boucle), puffs gaussiens texturés, opacité discrète, masque ciel uniquement

**Points techniques clés** :
- Masque chromatique « eau » : smoothstep((B−R+8)/16) - teintes chaudes (falaise B−R≈−24, sable ≈−22, arches ≈−36) immobiles
- Palette GIF **unique partagée** (calculée sur l'image moyenne des trames) + **dither=NONE** → fini le flicker de quantification
- Diagnostics par diff de trames : part du mouvement sur teintes chaudes 17 % → ~6 %
- Script de génération : `/tmp/opencode/make_v9.py` (à recopier dans le repo si souhaité)

## À valider par l'utilisateur

- [ ] Vitesse/amplitude de la fumée (opacité, course vers la cascade)
- [ ] Vitesse de chute des feuilles blanches
- [ ] Ampleur des rafales d'écume

## 16 nov. (suite) - itérations animation

- v10 : fumée en aller-retour → **refusé** : elle ne doit pas repartir à droite. Passage en **traversée linéaire** (droite → gauche, sans retour), boucle allongée.
- v11 : boucle **56 trames × 150 ms = 8,4 s** (sous-période eau = 28 trames = 2,8 s, phases imbriquées `i % 28`) ; fumée traverse en 5,6 s effectifs (2× plus lente) ; **écume du rivage étendue** à toute la dentelle sur le sable (dilution MaxFilter(51) ≈ 66 px), exclusions barquettes translucides + zone papiers ; fumée : alpha quantifié (20 niveaux) + palette 192 + largeur 800 → **2 Mo** (v10 faisait 33 Mo)
- v12 : **algue du bas-centre animée** (rect algues étendu x 30→1270, cluster jaune-vert ≈ (980-1140, 1450-1660)) ; **feuilles s'assombrissent en profondeur** (`out *= 1 - 0.16·m_pap·p`)
- v13 (FINALE) : assombrissement porté à 0.22. → `cascade-flow.gif` 2,1 Mo
- Script de génération : `/tmp/opencode/make_v12.py` (v13 = même script, facteur 0.22)

## 16 nov. (fin) - la bonne ligne d'eau

- Constat utilisateur : la zone animée à droite n'était pas le bord de mer (débordement du masque d'écume sur les nuages gris près du feu).
- **v16 (FINALE)** : couloir de côte défini par polyligne `(1230,190)→(1330,480)→(1400,790)→(1490,1040)→(1590,1270)→(1720,1480)→(1950,1678)` (±150 px + fondu 60 px) :
  - `m_foam` (glissement + rafales) restreint au couloir
  - bande de ressac = dilate(eau) ∧ dilate(sable|écume blanche) ∧ couloir, vague asymétrique (flot rapide / jusant lent, ±2,4 px, phase voyageant le long de la côte)
  - vérifié par diff de trames : la ligne blanche bouge sur toute sa longueur, sable/barquettes/nuages immobiles (9,5 % de pixels chauds = fumée en surimpression, normal)
  - 2,0 Mo - `cascade-flow.gif`

## 16 nov. (nouvelle source) - version finale sur `cascade-source.png`

- L'utilisateur a fourni l'**image originale propre** : `Screens/background ok.png` (2524×1674) → copiée dans le projet en **`cascade-source.png`** (source stable de tous les traitements). NB : le fichier annoté `Elise found this on 2026-11-16 à 13.01.11.png` contient le tracé rouge dessiné par l'utilisateur.
- **Tracé du serpentin extrait automatiquement** du tracé rouge (exclusion de la zone feu), ordonné par **chaînage plus-proche-voisin** (gère la section horizontale près de la barquette jaune), lissé, ré-échantillonné tous les 30 px, recalé 2532×1678 → 2524×1674 : `trace_final.npy` (84 points).
- **v17-v20** : bande du serpentin = ±15 px du tracé (doux, vague asymétrique ±2,5 px le long de la ligne, normales côté sable) ; pièges corrigés au passage :
  - la nappe claire + barquettes immergées prises pour des papiers → filtre de densité (GaussianBlur 25 + seuil 0,30/0,35) + **exclusions rect** (880-1430, 500-1050) et (1080-1490, 940-1460)
- **v20 FINALE : `cascade-flow.gif` 1,6 Mo** - vérifié par diff : serpentin animé sur toute sa longueur, barquettes/nappe/nuages immobiles, papiers + algues + cascade + fumée conformes.
- Script : `/tmp/opencode/make_v20.py`

## 16 nov. (v21) - deux serpenteins + corrections demandées

- **v21 FINALE : `cascade-flow.gif` 1,9 Mo** (source = `cascade-source.png`).
- **Barquette du haut immobile** : tracé tronqué (départ y ≥ 420, « le mouvement commence juste en dessous »), barquette exclue de la bande marine et de la fumée (le voile passe désormais **derrière** la dune/barquettes via exclusions dans `m_sky`, trajectoire relevée y 79→221).
- **Pixels gris statiques** : les 6 barquettes grises exclues des masques (bord interne à 12 px du tracé conservé vivant : `side_deep`).
- **Écume uniquement sur fond ocre/sable** : gate `sand_gate` (côté sable du tracé).
- **Feuilles : l'élément entier descend** - translation rigide en 2 temps : effacement à l'origine (remplissage par l'eau environnante `water_fill`) puis **redessin** du papier décalé (18 px, 2 cycles/boucle), assombrissement −22 % au fond.
- **Zone centrale du serpentin animée** : la cause était l'exclusion rect (1500-2080, 780-1640) qui recouvrait le tracé + le damping m_foam (0,8→0,5).
- **Nouveau : serpentin noir** (bord interne de la nappe, côté eau) extrait de l'image modèle fournie (`14.17.29.png`, lignes rouge+noire) : alignement modèle→source calé sur la ligne rouge (résidu 2,5 px), `trace_black_src.npy` (62 pts) ; **même vague/reflux** (asymétrique, ±2,5 px) en déphasage (+1,1 rad) - les deux serpenteins ondulent sans être synchrones.
- Script : `/tmp/opencode/make_v21.py`

## 16 nov. (v24-v26) - finalisation

- **v24** : zones vertes statiques (morceaux de barquette traversés par les serpenteins) appliquées à tous les masques via `bloc_statique` ; relâchement du filtre papiers → trop permissif (bords de nappe/barquettes bougeaient).
- **v25** : détection des feuilles par **composantes connexes** (ouverture morpho + étiquetage + seuil de taille 1500 px) - seuls les petits objets isolés (feuilles, y compris celle du milieu de l'image, zone `m_papiers` élargie à x ≤ 1550) couulent ; nappe et barquettes exclues structurellement.
- **v26 FINALE : `cascade-flow.gif` 1,9 Mo** - fumée **assombrie** (teinte rouille ×0,78) et nuage **agrandi** (rayons ×1,15, alpha +10 %).
- Vérif diff trames : les deux serpenteins animés sur toute leur longueur (y compris zone centrale), zones vertes ~statiques (84/63 px résiduels), barquettes et sable immobiles.
- Scripts : `/tmp/opencode/make_v26.py` (chaîne v21→v26 par patches successifs).

## 16 nov. (v27-v29) - corrections « eau trop sombre / barquette / silhouettes »

- **v27 (avorté)** : tentative de confinement vertical de la fumée - **abandonné** : l'utilisateur valide la fumée telle quelle (« garde le nuage de fumée supérieur, très bien ! »).
- **v28** : barquettes A/B (au-dessus du tracé) → exclusion **stricte** (`HARD_TRAYS`, plus de `side_deep`) ; papiers : gate resserré (L>196, d>−10), `water_fill` **texturé** (détail haute fréquence ×0,55 réinjecté), assombrissement 0,22→0,12, ouverture morpho MinFilter 3 et seuil CC 2200 (garde plus de vraies feuilles).
- **Bugs trouvés** : rects des silhouettes **inversés** (x/y échangés → d'immenses zones bougeaient, dont le livre) ; les silhouettes sont peintes en tons **froids** → le gate « corps chaud » les excluait toutes (masques vides).
- **v29 FINALE : `cascade-flow.gif` 1,6 Mo** - silhouettes : rects corrigés, oscillation 3,0/2,0 px déphasée par silhouette (vérifié : 640-770 px bougés par silhouette) ; barquette haute : 131 px résiduels (fumée en bord, validée).
- Script : `/tmp/opencode/make_v29.py`

## 16 nov. (v30-v32) - silhouettes verticales + feuilles

- **v30** : silhouettes humaines → oscillation **verticale pure** (montée/descente), même profil temporel que la vague du serpentin (flot rapide/jusant lent), phases décalées de 0,4 rad.
- **v31** : même ballotement appliqué à **tous** les éléments blancs de la zone eau : papiers (oscillent pendant leur chute) + feuilles moyennes flottantes (`m_float`, composantes CC 2200-8000 px, ballotement seul).
- **v32 FINALE : `cascade-flow.gif` 1,6 Mo** - retour à **1 cycle de chute par sous-période** (4,2 s, au lieu de 2 → fini l'effet « rebond ») et suppression du ballotement séparé sur les papiers (chute lisse) ; le ballotement reste sur les feuilles flottantes et les silhouettes.
- Cascade, fumée, bord de mer : **inchangés** (validés par l'utilisateur).
- Script : `/tmp/opencode/make_v32.py`

## 16 nov. (v33) - tous les éléments cerclés rose

- L'utilisateur a annoté l'image (cercles roses = éléments clairs à traiter, cercles verts = les 2 modèles + zones statiques), fichier `14.28.33.png` (2468×1626) → extraction des ellipses par CC à quart de résolution : **18 ellipses roses** → `pink_boxes.npy`, recalées ×1,0227/×1,0295.
- `m_pink` = union des ellipses (∩ gate clair L>175, d>−14, flou 1,2) ; **`m_paper_all = max(m_pap0, m_pink)`** : tous les éléments roses reçoivent le traitement des modèles (chute 18 px/4,2 s avec effacement/remplissage/redessin, assombrissement 0,12).
- `m_float` (feuilles moyennes flottantes) masque `m_pink` pour éviter le doublon ; zones vertes statiques respectées.
- **v33 FINALE : `cascade-flow.gif` 3,1 Mo** - vérifié par diff : les 18 zones roses animées, modèles OK, zones vertes et barquettes immobiles.
- Script : `/tmp/opencode/make_v33.py`

## 16 nov. (v34-v35) - ellipses roses individuelles

- v33 (union des ellipses dans `m_paper_all` avec effacement/redessin) : **rejetée** - taches de remplissage moches, glissement de bloc. v34 (bande fusionnée unique) : **rejetée** - 67 000 px glissaient d'un bloc à gauche (« oulala »).
- **v35 FINALE : `cascade-flow.gif` 3,2 Mo** - chaque ellipse rose est **individuelle** :
  - chaque bande (gate « éléments clairs » L>165, d>−16 : seule la feuille bouge, pas l'eau ouverte autour) 
  - glissement vertical 16 px + **transparence croissante** avec la profondeur (opacité 100 % → 45 %, quantifiée en 12 niveaux)
  - **phases décalées** (k×0,6 rad) : chaque élément suit son propre cycle, aucun mouvement de calque
  - exclusions : papiers déjà animés (`m_pap0`) + feuilles flottantes (`m_float`)
- Diagnostics v35 : les 4 zones tests bougent individuellement (810/1947/134/81 px), cascade et barquettes inchangées par rapport à v32 (bruit de palette résiduel uniquement).
- Script : `/tmp/opencode/make_v35.py`

## 16 nov. (soir) - conservation des fichiers + formats de diffusion

**Nouvelle consigne permanente : plus aucun fichier écrasé - numérotation incrémentale.**

- Les 7 derniers GIFs archivés dans le projet : `cascade-flow-01.gif` (v30) → `cascade-flow-07.gif` (v36).
- Incident corrigé : la génération v36 avait écrasé `cascade-v35.gif` (patch de chemin non appliqué) - la v35 originale 800px était sauvegardée dans `cascade-flow.gif`, restaurée en `-06`.
- **v37 = `cascade-flow-08.gif` (720 px, palette 192 couleurs restaurée)** - la dégradation cascade/clapotis venait de la palette 160 couleurs (banding), le mouvement n'avait jamais changé. ~2,8 Mo.
- **`cascade-flow-08.mp4`** : encodage H.264 (libx264, CRF 22, yuv420p, 30 i/s, faststart) depuis les trames **pleine qualité** via ffmpeg (imageio-ffmpeg ; les trames font 720×479, scale → 720×478 pour H.264). **485 Ko** - format requis par Instagram/TikTok.
- Scripts recopiés dans le projet ? à faire si demandé ; génération : `/tmp/opencode/make_v37.py`.
- Prochaine étape suggérée : export carré 1:1 (IG feed) / vertical 9:16 (stories/TikTok) en MP4.

## 16 nov. (v38) - retour v32 + ellipses roses façon silhouettes

- Supprimés à la demande : `cascade-flow-05/06/07.gif` (restent : 01, 02, 03, 04, 08, 09).
- **v38 = `cascade-flow-09.gif` (800 px, 2,4 Mo) + `cascade-flow-09.mp4` (720×478, 30 i/s, 400 Ko)** :
  - base **strictement v32** (cascade-flow-03, la version validée)
  - ellipses roses : oscillation verticale **identique aux silhouettes** (±2,2 px, profil serpentin `sin(t−0,45·sin t)`, phases k×0,4, opacité constante - pas de fondu, pas de chute)
  - vérifié : corrélation de structure 0,93 hors zones roses → seul un re-mapping de palette (invisible), **aucun autre mouvement**
- Script : `/tmp/opencode/make_v38.py`

## 16 nov. (v39-v41) - fidélité absolue à flow-03

- Problème : v38 (flow-09) recalculait la palette GIF → dégradés (cascade, transition au-dessus des clapotis) légèrement altérés vs la référence.
- v39 : ré-quantification RGB→palette - rejetée (PIL non réversible, 75k px dérivent).
- v40 : espace d'indices - échec (PIL renvoie des trames RGB composées après la première).
- **v41 = `cascade-flow-10.gif` (2,5 Mo) + `cascade-flow-10.mp4` (430 Ko)** :
  - décodage RGB exact des trames de **cascade-flow-03** (référence)
  - ballottement des ellipses roses (mouvement silhouettes) appliqué sur ces trames
  - remapping **index-exact** : LUT couleur→index de la palette v32 pour les pixels intacts, plus proche couleur uniquement dans les bandes
  - **vérifié : 0 pixel de différence hors zones roses** sur les trames testées - cascade, clapotis et tout le reste strictement identiques à flow-03
- Script : `/tmp/opencode/make_v41.py`

## 16 nov. (v42-v46) - dernier essai : fumée + barquette, et le VRAI bug trouvé

- v42/v43 (cascade-flow-11, 12) : ajout fumée compagnon (haut) + effets de mer sur la barquette bas-centre (dérive ±3 px, scintillement 3,5 %, brume - **pixels blancs/clairs statiques** via gate).
- L'utilisateur voit des pixels de ciel animés au centre-haut → diagnostic par étapes : **le vrai coupable était un bug d'ordre d'arguments** dans la construction des bandes roses (make_v38 : `(x0,y0,x1,y1)` donné à `rect_mask(x0,x1,y0,y1)`) → l'ellipse `(0,625,49,708)` devenait un rect géant couvrant tout le haut-gauche (cause réelle des soucis « cascade sautée » depuis flow-09 !). Corrigé à la source + backup `make_v38-buggy-backup.py`.
- v44/v45 : compagnon confiné (fondu dur sous y≈120 orig) - **ciel = 0 px modifié** ✓ ; 7/18 ellipses réellement actives (les autres n'ont pas de contenu clair - gate L>165 + contraste local).
- **v46 FINALE : `cascade-flow-12.gif` (3,6 Mo) + `cascade-flow-12.mp4` (527 Ko)** - barquette : 33 715 px animés, fumée haute discrète, ellipses sur contenu clair, ciel/cascade strictement identiques à flow-03.
- Scripts : `/tmp/opencode/make_v46.py` (chaîne v41→v46), source corrigée `make_v38.py`.

## 16 nov. (clôture) - retour à flow-10

- **cascade-flow-12 (v46) rejetée** : le quadrant bas-droit était trop modifié (les effets de mer sur la barquette couvraient une large zone d'eau) ; les feuilles préférées dans la version précédente.
- **`cascade-flow.gif` = restauration de `cascade-flow-10`** (v41, la version validée « oooh c'est super ») - archive intacte, jamais écrasée.
- Statut final : flow-10 = version courante ; flow-01…12 archivés.

## 16 nov. (v47) - flow-10 + ciel statique

- Constat : flow-10 (v41) contient encore les bandes d'ellipses mal placées (bug d'ordre d'arguments corrigé plus tard dans make_v38.py) - dont le rect géant animant le ciel/pale mer au-dessus de la cascade.
- **`cascade-flow-13`** : flow-10 **inchangé** partout, SAUF le bloc haut-gauche (x<1150, y<500 orig, fondu 30) **figé aux valeurs de la référence flow-03** - traitement index-exact sur les trames décodées de l'archive.
- Vérifié : bloc figé = 0 px vs flow-03 ; zone feuilles = 0 px vs flow-10.
- `cascade-flow.gif` = flow-13 (courant). **flow-13 : GIF 2,3 Mo + MP4 423 Ko.** Script : `/tmp/opencode/make_v47.py`.

## 16 nov. (v48) - clapotis sur la ligne orange

- Ligne **orange** extraite de l'image annotée (filtre strict R>225, B<90 - la sardine de la barquette jaune écartée), chaînage NN, 58 points, de (1150, 396) à (2173, 1630) - recalage modèle→source via l'alignement rouge.
- **`cascade-flow-14`** = flow-13 + ressac identique aux serpenteins le long de la ligne orange : bande ±12 px (fondu 20), vague asymétrique ±2,5 px (flot rapide/jusant lent), crête voyageuse (λ 280 px), normales côté sable, **exclusions barquettes (side_deep 12 px) + zones vertes statiques**.
- Vérifié : ciel = 0 px modifié, hors bande = ~130 px (fondu), dans bande ≈ 3 200 px animés.
- **flow-14 : GIF 2,5 Mo + MP4 435 Ko.** `cascade-flow.gif` = flow-14 (courant). Script : `/tmp/opencode/make_v48.py`.

## 16 nov. (v49) - ligne orange visible

- flow-14 : ressac orange appliqué mais **imperceptible** (±2,5 px sur contenu lisse).
- **`cascade-flow-15`** : amplitude **doublée** (±5 px) + **respiration lumineuse** ±5 % liée à la vague - le mouvement devient lisible même sur l'eau lisse.
- Vérifié : ≈ 5 460 px animés dans la bande (vs 3 200 avant), ciel propre (les 65 px détectés = le début voulu de la ligne près de la barquette haute), hors bande ≈ 200 px (fondu).
- **flow-15 : GIF 2,6 Mo + MP4 444 Ko.** `cascade-flow.gif` = flow-15 (courant). Script : `/tmp/opencode/make_v49.py`.

## 16 nov. (v50-v51) - ligne orange bien visible

- v50 (±4 px = amplitude du bord des vagues) : **rejetée** - « encore bien trop subtil ».
- **`cascade-flow-16` (v51)** : bande élargie ±16 px (fondu 24), va-et-vient **±8 px**, **crête lumineuse voyageuse** (assombrissement 35 % / éclaircissement +35 % +18 sur la crête `sin²`), respiration ±8 %.
- Vérifié : ≈ 8 300 px animés dans la bande, hors bande ~200 px (fondu), ciel propre.
- **flow-16 : GIF 2,7 Mo + MP4 452 Ko.** `cascade-flow.gif` = flow-16 (courant). Script : `/tmp/opencode/make_v51.py`.

## 16 nov. (v52-v54) - clapotis SUR la barquette du premier plan

- Découverte : la ligne orange traverse la barquette du bas, mais mes exclusions « barquettes/zones vertes » coupaient la bande à ces endroits → invisible.
- v52 : exclusions retirées (10 553 px animés) - mais la barquette du HAUT se déformait aussi.
- **`cascade-flow-17` (v54)** : exclusions **durcies et élargies** sur les 2 barquettes hautes (feather 8, rect élargi) ; la bande orange anime librement la barquette du premier plan (±8 px + crête lumineuse + respiration).
- Vérifié : barquettes hautes = 24/1 px (bruit), ciel = 0-14 px, zone bas = 5 767 px animés, bande = ~10 100 px.
- **flow-17 : GIF 2,8 Mo + MP4 460 Ko.** `cascade-flow.gif` = flow-17 (courant). Script : `/tmp/opencode/make_v54.py`.

## 16 nov. (v55) - ligne orange au bon endroit

- Cause de l'invisibilité persistante : le recalage de la ligne orange utilisait la transformée de l'image 14.17.29 (décalage +19/+31), alors que l'échelle pure (validée par les cercles roses de la même image 14.28.33) était correcte → **ligne décalée de ~34 px** (la bande battait à côté de votre tracé).
- **`cascade-flow-18`** : polyline recalée (début (1168, 378), fin (2224, 1655)), même traitement (±8 px + crête lumineuse + respiration, barquettes hautes figées).
- Vérifié : ciel = 0, hors bande ~200 px (fondu), bande ≈ 10 500 px animés.
- **flow-18 : GIF 2,8 Mo + MP4 463 Ko.** `cascade-flow.gif` = flow-18 (courant). Script : `/tmp/opencode/make_v55.py`.

## 16 nov. (v56-v57) - la vague passe PAR-DESSUS (submersion voyageuse)

- Découverte : les patches v56 (onde lumineuse) n'avaient **jamais été appliqués** (remplacements silencieux non matchés) - v56/v57 exécutaient toujours le déplacement ±8 px → déformation des parties blanches.
- Réécriture chirurgicale du bloc : **submersion voyageuse** - la crête (profil flot/jusant) **recouvre la ligne et ses 2 parties blanches** d'eau échantillonnée côté mer (offset 10-20 px), à 92 % au pic, puis se retire. **Direction inversée : la vague voyage de droite à gauche** (`th = t − s_o/λ`).
- Vérifié visuellement (trames) : les parties claires sont lavées d'un lavis teal au passage puis dégagées ; ciel = 0 ; hors bande ~150 px.
- **flow-19 : GIF 2,7 Mo + MP4 453 Ko.** `cascade-flow.gif` = flow-19 (courant). Script : `/tmp/opencode/make_v57.py`.

## 16 nov. (clôture des tests) - VERROUILLAGE FINAL

- « On s'éloigne. On arrête les tests. » - arrêt des essais sur le serpentin orange.
- **VERSION FINALE = flow-17** (= flow-16 [animation orange ±8 px + crête lumineuse + respiration] **+ barquettes du haut verrouillées** [exclusions durcies, 24 px résiduels]).
- `cascade-flow.gif` = copie de `cascade-flow-17.gif`. Le serpentin orange est **abandonné** (jamais validé).
- Fichiers finaux de distribution : `cascade-flow-17.gif` (2,8 Mo) + `cascade-flow-17.mp4` (460 Ko).

## 16 nov. (vraie clôture) - flow-20 = v16 + verrou haut

- Correction de compréhension : flow-17 **déformait la barquette du bas** (v52 avait retiré TOUTES les exclusions ; v53/54 n'avaient remis que celles du haut). Flow-16, lui, protégeait la barquette du bas (exclusions d'origine intactes).
- **`cascade-flow-20` (v58) = make_v51 (flow-16) STRICTEMENT INCHANGÉ** (ligne d'origine, ±8 px + crête lumineuse + respiration, TOUTES les exclusions d'origine - barquette du bas protégée) **+ verrouillage durci des 2 barquettes hautes uniquement**.
- Vérifié : barquette haute 333 px → 24 px (verrou) ; **barquette du bas = 0 px de différence avec flow-16**.
- **VERSION FINALE : `cascade-flow-20.gif` (2,7 Mo) + `cascade-flow-20.mp4` (450 Ko).** `cascade-flow.gif` = flow-20. Script : `/tmp/opencode/make_v58.py`.

## 17 nov. - formats sociaux (livrés)

- Choix utilisateur : **recadré cascade** pour les 3 formats (via question).
- **`cascade-flow-20-instagram-feed.mp4`** - carré 1:1 (1080×1080), cascade au tiers gauche, recadrage 531×531 + agrandissement + unsharp mask. 2,1 Mo.
- **`cascade-flow-20-story-tiktok.mp4`** - vertical 9:16 (1080×1920), recadrage 298×531 (≈ x 180-1120 orig), unsharp mask. 2,6 Mo. Valide pour Story Instagram ET TikTok.
- Les 4 variantes de test conservées : `cascade-flow-20-sq_full/sq_crop/v_full/v_crop.mp4`.
- Qualité : trames 800 px agrandies (×2 carré, ×3,6 vertical) + accentuation - correcte pour mobile ; une relance complète du pipeline en 1600 px natif reste possible si netteté parfaite souhaitée.
