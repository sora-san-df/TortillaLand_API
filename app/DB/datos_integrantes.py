#python
from typing import List
#Models 
from ..Models import Integrantes_model




integrantes = Integrantes_model.Integrantes
canal = Integrantes_model.Streamers

#data de los integrantes
db: List[integrantes]=[
    #El_Mariana
    integrantes(
        nombre_real="Osvaldo Palacios Flores",
        foto="https://i.ibb.co/thTwKnz/EL-Mariana.jpg",
        nombre_en_juego="ELMariana",
        integrantes_id="fe6b1ffa-b9f7-4d9e-bd8e-bb52df9b0b11",
        edad="24 años",
        pais_origen="Mexico",
        pais_residencia="Mexico"
    ),
    #Spreen 
    integrantes(
        nombre_real="Ivan Raul Buhajeruk Fernández",
        foto="https://i.ibb.co/NW3QSdq/Spreen.jpg",
        nombre_en_juego="SpreenDMC",
        integrantes_id="55e33642-17ab-498a-95e9-9bb3cb19ca6c",
        edad="22 años",
        pais_origen="Argentina",
        pais_residencia="Argentina"
    ),
    #Karchez
    integrantes(
        nombre_real="Carlos Sánchez",
        foto="https://i.ibb.co/MBnfkVF/Karchez.jpg",
        nombre_en_juego="Karchez",
        integrantes_id="0cb5b175-4b1c-4ec5-af2e-b02c2c2958cf",
        edad="22 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Axoxer
    integrantes(
        nombre_real="Axozer",
        foto="https://i.ibb.co/z8gg5Ck/Axocher.jpg",
        nombre_en_juego="aXoZer",
        integrantes_id="2bc9b731-72ed-4a37-b0e6-89de3093b053",
        edad="20 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #DJMARIIO
    integrantes(
        nombre_real="Mario Alonso Gallardo",
        foto="https://i.ibb.co/SmRYkd3/DjMariio.jpg",
        nombre_en_juego="DjMaRiiO",
        integrantes_id="554a80f8-8941-420c-9408-746b99f9b3b2",
        edad="32 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Biyin
    integrantes(
        nombre_real="Sara Modelo",
        foto="https://i.ibb.co/vwTkDVG/Biyin.jpg",
        nombre_en_juego="Biyin_",
        integrantes_id="c693964a-2a98-4090-a907-62b033fca708",
        edad="31 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Arigameplays
    integrantes(
        nombre_real="Abril Abdamari Garza Alonzo",
        foto="https://i.ibb.co/VVVxXjL/Ari.jpg",
        nombre_en_juego="ArideGuarnizo",
        integrantes_id="afb650db-7c16-4477-84ee-c2ea601b9791",
        edad="24 años",
        pais_origen="Mexico",
        pais_residencia="Mexico"
    ),
    #Carreraaa
    integrantes(
        nombre_real="Rodrigo Carrera",
        foto="https://i.ibb.co/t41MYWN/Carrera.jpg",
        nombre_en_juego="carreracraft11",
        integrantes_id="a9f869a8-9b17-4b70-86ef-a9b6e0c62ad5",
        edad="22 años",
        pais_origen="Argentina",
        pais_residencia="Argentina"
    ),
    #Carola
    integrantes(
        nombre_real="Fedor Chernyshev",
        foto="https://i.ibb.co/BCVcw1G/Caroola.jpg",
        nombre_en_juego="ElCarola",
        integrantes_id="0f99e34b-0603-4097-a4db-fcd9994e92f4",
        edad="26 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Pol <3
    integrantes(
        nombre_real="Pol Turrents",
        foto="https://i.ibb.co/wgGqdZw/pol.jpg",
        nombre_en_juego="Polispol1",
        integrantes_id="697d8b89-4ae1-478c-906a-9f0a441a0d79",
        edad="46 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Auron mi niño
    integrantes(
        nombre_real="Raúl Álvarez Genes",
        foto="https://i.ibb.co/B2kqrzH/Auron.jpg",
        nombre_en_juego="Auron",
        integrantes_id="1fe60389-9bd6-4a48-8dbe-031ba5428135",
        edad="34 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Juano
    integrantes(
        nombre_real="Juan Sebastían Guarnizo Algarra",
        foto="https://i.ibb.co/WnRwLyW/Juan.jpg",
        nombre_en_juego="ElJuaniquilador",
        integrantes_id="4d3bb25f-e397-4fdf-bc3d-625dc132cbfa",
        edad="25 años",
        pais_origen="Colombia",
        pais_residencia="Mexico"
    ),
    #Aroyitt
    integrantes(
        nombre_real="Aroia García",
        foto="https://i.ibb.co/fD8Dm76/Aroyitt.jpg",
        nombre_en_juego="Aroyitt",
        integrantes_id="e09c7331-ce4d-4813-be35-0273eebe17fe",
        edad="29 años",
        pais_origen="España",
        pais_residencia="Andorra"
    ),
    #Mayichi
    integrantes(
        nombre_real="Mayichi",
        foto="https://i.ibb.co/n1BTNtJ/Mayichi.jpg",
        nombre_en_juego="Mayichi",
        integrantes_id="7b4a944b-d214-4538-84e7-705dcd3027a2",
        edad="26 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Ibai
    integrantes(
        nombre_real="Ibai Llanos Garatea",
        foto="https://i.ibb.co/ykJJmbR/Ibai.jpg",
        nombre_en_juego="Ibai",
        integrantes_id="9b9221dc-df3d-4635-8f77-f584d5a4fdd6",
        edad="27 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Focus
    integrantes(
        nombre_real="Focus",
        foto="https://i.ibb.co/MGDTH30/Focus.png",
        nombre_en_juego="xTheFocuSx",
        integrantes_id="60e33ee6-98b4-42a4-a6ac-d0cd11a6b3da",
        edad="Desconocido(creo)",
        pais_origen="España",
        pais_residencia="Desconocido"
    ),
    #Reborn 
    integrantes(
        nombre_real="Reborn",
        foto="https://i.ibb.co/hcFC0Pr/Reborn.jpg",
        nombre_en_juego="rebornislive",
        integrantes_id="fb848cc5-ef19-4f66-a99c-2d1684709160",
        edad="27 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Tanizen 
    integrantes(
        nombre_real="Tanizen",
        foto="https://i.ibb.co/gzBnMzz/tanizen.jpg",
        nombre_en_juego="Tanizen",
        integrantes_id="f905bdcb-a985-4571-b697-146c8057c22a",
        edad="33 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #BarbeQ
    integrantes(
        nombre_real="Ernesto Folch Casanoves",
        foto="https://i.ibb.co/Hd24CvK/Barbesito.jpg",
        nombre_en_juego="Barbesito",
        integrantes_id="862b9ec0-c89b-43ba-9d53-c68d5ee38fab",
        edad="33 años",
        pais_origen="España",
        pais_residencia="España" 
    ),
    #BarcaGamer
    integrantes(
        nombre_real="Diego Martin Balsa Rial",
        foto="https://i.ibb.co/6NvHnNM/Barca.jpg",
        nombre_en_juego="SoyBarcaGamer",
        integrantes_id="c4423f00-f746-4489-8f60-be0bcc4f5f6c",
        edad="22 años",
        pais_origen="Uruguay",
        pais_residencia="Mexico"
    ),
    #Cristini
    integrantes(
        nombre_real="Cristina López Peréz",
        foto="https://i.ibb.co/sJTw35n/Crisitnini.jpg",
        nombre_en_juego="Cristinini",
        integrantes_id="c7e88a8e-e520-4d9b-a94c-579e9b60b33b",
        edad="32 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Pato
    integrantes(
        nombre_real="David(posiblemente)",
        foto="https://i.ibb.co/KNbyw5m/Pato.jpg",
        nombre_en_juego="PatoDeAqualand",
        integrantes_id="b58f6b66-fcd5-458c-8dc2-7f5aaeb91896",
        edad="Desconocido",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Perxita
    integrantes(
        nombre_real="Jaume Cremades",
        foto="https://i.ibb.co/8sdMcm4/perxitaa.jpg",
        nombre_en_juego="Srperxitaa",
        integrantes_id="370d18f6-fa5a-4b31-a35e-8663104f17cf",
        edad="31 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Violeta G 
    integrantes(
        nombre_real="Violeta",
        foto="https://i.ibb.co/hBQBKm0/Violeta.jpg",
        nombre_en_juego="VioletaG",
        integrantes_id="6e708be2-5f2b-4a57-abfa-c043647a562a",
        edad="30 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #Imantado 
    integrantes(
        nombre_real="Imantado",
        foto="https://i.ibb.co/pnBY1Sg/Imantado.jpg",
        nombre_en_juego="imantado",
        integrantes_id="5854801e-e3e1-4c8f-9f54-b3a7887724a8",
        edad="25 años",
        pais_origen="España",
        pais_residencia="España"
    ),
    #DessT3
    integrantes(
        nombre_real="Christian Desst",
        foto="https://i.ibb.co/jwKshKn/Destt3.jpg",
        nombre_en_juego="D3SST3",
        integrantes_id="655eaf1c-e804-43e3-b91e-cf0c64c72687",
        edad="Desconocido",
        pais_origen="Desconocido",
        pais_residencia="Desconocido"
    ),
    #Komanche
    integrantes(
        nombre_real="Komanche",
        foto="https://i.ibb.co/RYC8XtH/komanche.jpg",
        nombre_en_juego="ElKomanche",
        integrantes_id="46b13b3b-d115-4bd0-bc3e-8b8297ede41d",
        edad="26 años",
        pais_origen=" El Salvador",
        pais_residencia="Mexico"
    ),
    #Zorman 
    integrantes(
        nombre_real="Norman Vivas",
        foto="https://i.ibb.co/s6CNhjV/Zorman.jpg",
        nombre_en_juego="Zormanos",
        integrantes_id="767ce116-1418-4d60-a428-ce9f0e244c83",
        edad="33 años",
        pais_origen=" España",
        pais_residencia="España"
    ),
    #Ampeter
    integrantes(
        nombre_real="Andrés López  Ruitorta",
        foto="https://i.ibb.co/nw8bCkN/ampeter.jpg",
        nombre_en_juego="Ampeter",
        integrantes_id="9e1b7965-570f-455d-8bc0-1084e292701b",
        edad="23 años",
        pais_origen=" España",
        pais_residencia="Andorra"
    ),
    #Jacky
    integrantes(
        nombre_real="Ricardo",
        foto="https://i.ibb.co/sjfkkyP/Jacky.png",
        nombre_en_juego="JackyMaster",
        integrantes_id="1c16111e-b5c0-458c-8c88-201534cfa4e4",
        edad="28 años",
        pais_origen=" España",
        pais_residencia="España"
    ),
    #Genesis
    integrantes(
        nombre_real="Genesis",
        foto="foto.png",
        nombre_en_juego="Th3Genesis",
        integrantes_id="d3b2222f-54d9-41bd-8f43-10fd839620e5",
        edad="Desconocido",
        pais_origen=" España",
        pais_residencia="España"
    ),
    #Jabu
     integrantes(
        nombre_real="Jabu",
        foto="https://i.ibb.co/MDrQFBs/Jabu6.jpg",
        nombre_en_juego="Jabu6",
        integrantes_id="64ebd838-3722-4522-b670-47a0c49dfc3a",
        edad="Desconocido",
        pais_origen="Desconocido",
        pais_residencia="Desconocido"
    ),
    #DeqiuV
    integrantes(
        nombre_real="Deqiuv",
        foto="https://i.ibb.co/X53K3bY/Deqiuv.jpg",
        nombre_en_juego="DeqiuVKLK",
        integrantes_id="051e5bdc-b286-4e86-9762-b6038b863be6",
        edad="Desconocido",
        pais_origen="Desconocido",
        pais_residencia="Desconocido"
    ),
    #Betra
    integrantes(
        nombre_real="Fran Ciancioci",
        foto="https://i.ibb.co/fkGFDN2/Betra.jpg",
        nombre_en_juego="Betra1",
        integrantes_id="02fdae9e-72f1-4794-83fb-98925a7fda6f",
        edad="Desconocido",
        pais_origen="Argentina",
        pais_residencia="Argentina"
    )

]
#canles de los integrantes
canales: List[canal]=[

    canal(
        canal_twitch="ELMARIANA",
        canal_image="https://i.ibb.co/1qPJxch/elmariana.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="ELSPREEN",
        canal_image="https://i.ibb.co/tHR9nWC/spreen.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="KARCHEZ",
        canal_image="https://i.ibb.co/X3sZj45/karchez.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="AXOZER",
        canal_image="https://i.ibb.co/FbNmdS3/axozer.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="DJMARIIO",
        canal_image="https://i.ibb.co/rkqvQcx/djmariio.jpg",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="BIYIN_",
        canal_image="https://i.ibb.co/7pFW0rQ/biyin.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="ARIGAMEPLAYS",
        canal_image="https://i.ibb.co/wzLcPrm/ari.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="CARRERAAA",
        canal_image="https://i.ibb.co/XtdTvS8/carreraaa.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="CAROLA",
        canal_image="https://i.ibb.co/NY8G9zh/carola.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="POLISPOL1",
        canal_image="https://i.ibb.co/zXTTpG1/pol.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="AURONPLAY",
        canal_image="https://i.ibb.co/0ychHGR/auron.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="JUANSGUARNIZO",
        canal_image="https://i.ibb.co/wYzwBmv/juano.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="AROYITT",
        canal_image="foto.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="MAYICHI",
        canal_image="https://i.ibb.co/WVySW6w/mayichi.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="IBAI",
        canal_image="https://i.ibb.co/27zv1zR/ibaisito.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="XXXTHEFOCUSXXX",
        canal_image="https://i.ibb.co/jMr5QMM/foucs.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="REBORN_LIVE",
        canal_image="https://i.ibb.co/3NCdhqr/reborno.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="TANIZEN",
        canal_image="https://i.ibb.co/jL6pf9p/tani.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="ERNESBARBEQ",
        canal_image="https://i.ibb.co/VQh7fL6/barbesito.jpg",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="BARCAGAMER",
        canal_image="https://i.ibb.co/kxyCn2V/barca.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),

     canal(
        canal_twitch="IAMCRISTININI",
        canal_image="https://i.ibb.co/mhMstQq/cristinini.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="PATODEAQUALAND",
        canal_image="https://i.ibb.co/WfWTLLv/patooo.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="PERXITAA",
        canal_image="https://i.ibb.co/XW5TM3F/perxas.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="VIOLETAG",
        canal_image="https://i.ibb.co/KrSTYY3/violeta.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="IMANTADO",
        canal_image="https://i.ibb.co/jwFGHCZ/imantado.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
     canal(
        canal_twitch="DESST3",
        canal_image="https://i.ibb.co/Y7f8Mp6/desst3.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="KOMANCHE",
        canal_image="https://i.ibb.co/ZGWXqkX/komanche.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="ZORMANWORLD",
        canal_image="https://i.ibb.co/WpJyPqP/zorman.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="ZORMANWORLD",
        canal_image="foto.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="COOLIFEGAME",
        canal_image="https://i.ibb.co/vxpwQ4B/coolifegame.png",
        pueblo="pueblo verde",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="GTV_GENESIS",
        canal_image="https://i.ibb.co/31v0ZKf/genesis.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="JABU06",
        canal_image="https://i.ibb.co/fdt94Mh/jabu.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="DEQIUV",
        canal_image="https://i.ibb.co/PtGQJvj/deqiuv.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),
    canal(
        canal_twitch="BETRA",
        canal_image="https://i.ibb.co/KwYkDr2/betra.png",
        pueblo="pueblo naranja",
        temporada_tortilla="2"
    ),

]
#tortillass en el juego 
