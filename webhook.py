from dhooks import Webhook, Embed




hook = Webhook('https://discord.com/api/webhooks/774249770130210837/OhYICZEBNUTrx1EhVBax1Tbg4qHp6XUM3R7W0PjgTrJrwXM-E5BcYVAJ0TmIXJTWVIxV')



embed = Embed(
        description='**NUOVO LOGBOOK**:blue_book:',
        color=0x5CD8F0,
        timestamp= 'now')




image1 = 'https://img2.pngio.com/download-free-png-log-book-png-6-png-image-dlpngcom-logbook-png-217_276.png'

image2 = 'https://cb28online.files.wordpress.com/2018/01/galaxy-dx-33hp2-10-meter-mobile-ham-radio.png'

image3= 'https://img.favpng.com/1/12/22/walkie-talkie-computer-icons-pmr446-clip-art-png-favpng-cLWgMqc9hn9mcquSEA2f7qHBd.jpg'

image4 = 'https://lesficbardawards.com/uploads/1/1/5/6/115665537/561455f5067d7b15d996a14a_orig.gif'

image5 = 'https://lh4.googleusercontent.com/GYTcjJVtXPokLSD0Y0qEcjjcTKtp2swUcrZ-BZmgc1GSweBwsIHZkt1_ssock8Dl0Btz6IM6Sx-d-ExPEcLguP-mxf-cP_3eIIb0NvegIgyzYHFeHJVK3LD00RXsSg=w217'



embed.set_author(name='GRO News ', icon_url=image4)
embed.add_field(name=' **PER COMPILARE IL LOGBOOK** :flag_it:\n:flag_gb:      :flag_fr:      :flag_es:      :flag_de:       :flag_ru:      :flag_eu:', value='**CLICCA SUL LINK** :arrow_down:\n<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScoC0D2L5y8Sl6zQrmxM9qjCWvLZye6ROROOJC3RXV4tfKLaQ/viewform?embedded=true" width="640" height="2434" frameborder="0" marginheight="0" marginwidth="0">Caricamento…</iframe')
embed.add_field(name='**SEGUITECI** :eyes:', value=':100: Rimanete con noi per essere aggiornati sul Server e sulle ultime di tecnologia :100:')
embed.set_footer(text='Data invio', icon_url=image4)



embed.set_thumbnail(image4)
embed.set_image(image4)



hook.send(embed=embed)
print('News Inviata')
