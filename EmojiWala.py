import discord
from discord.ext import commands
from random import randint
import config

client = commands.Bot(command_prefix="~")
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=' ~help'))
    print("Bot is ready..")


@client.command()
async def ew(ctx, *, q=""):

    await ctx.channel.purge(limit=1)

    user_name = ctx.author.name

    if q == "":
        await ctx.send(f"** **\n**{user_name}:** At least write something. :sweat_smile:")
    else:
        string = q.split()
        flag = True
        final = ""
        for sub in string:
            for char in sub.strip():
                if char.isalpha():
                    final = final + ":regional_indicator_" + char.lower() + ": "
                elif char.isdigit():
                    final = final + ":" + {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}[char] + ": "
                else:
                    flag = False
                    break
            if not flag:
                break
            final = final + "  "

        if flag:
            await ctx.send(f"** **\n**{user_name}:**")
            await ctx.send(f"{final}")
        else:
            await ctx.send(f"** **\n**{user_name}:** Please use Alphabets and Numbers only!! :face_with_raised_eyebrow: ")


@client.command()
async def eh(ctx, *, q=""):

    await ctx.channel.purge(limit=1)

    if q == "":
        await ctx.send(f"** **\n At least write something. :sweat_smile:")
    else:
        string = q.split()
        flag = True
        final = ""
        for sub in string:
            for char in sub.strip():
                if char.isalpha():
                    final = final + ":regional_indicator_" + char.lower() + ": "
                elif char.isdigit():
                    final = final + ":" + {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}[char] + ": "
                else:
                    flag = False
                    break
            if not flag:
                break
            final = final + "  "

        if flag:
            await ctx.send(f"** **\n")
            await ctx.send(f"{final}")
        else:
            await ctx.send(f"** **\n Please use Alphabets and Numbers only!! :face_with_raised_eyebrow: ")


@client.command()
async def en(ctx, *, q=""):

    await ctx.channel.purge(limit=1)

    user_name = ctx.author.name

    if q == "":
        await ctx.send(f"** **\n**{user_name}:** At least write something. :sweat_smile:")
    else:
        string = q.split()
        flag = True
        lst = []
        for sub in string:
            final = ""
            for char in sub.strip():
                if char.isalpha():
                    final = final + ":regional_indicator_" + char.lower() + ": "
                elif char.isdigit():
                    final = final + ":" + {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}[char] + ": "
                else:
                    flag = False
                    break
            if not flag:
                break
            lst.append(final)

        if flag:
            await ctx.send(f"** **\n**{user_name}:**")
            for i in lst:
                await ctx.send(f"{i}")
        else:
            await ctx.send(f"** **\n**{user_name}:** Please use Alphabets and Numbers only!! :face_with_raised_eyebrow: ")


@client.command()
async def wg(ctx, *, q=""):

    await ctx.channel.purge(limit=1)

    user_name = ctx.author.name

    if q == "":
        await ctx.send(f"** **\n**{user_name}:** At least write something. :sweat_smile:")
    else:
        string = q.strip()
        flag = True
        final = ""
        for char in string:
            if char.isalpha() or char.isdigit() or char == " ":
                final = final + char.lower()
            else:
                flag = False
                break
        k = final.strip().split()
        ml = max(map(len, k))

        if flag:
            await ctx.send(f"** **\n**{user_name}:**")
            op = ""
            for v in k:
                op += ":blue_square: "*(ml-len(v))
                for i in v:
                    if i.isdigit():
                        op = op + ":" + {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}[i] + ": "
                    else:
                        op = op + ":regional_indicator_" + i + ": "
                op = op + "\n"
            await ctx.send(op)
        else:
            await ctx.send(f"** **\n**{user_name}:** Please use Alphabets and Numbers only!! :face_with_raised_eyebrow: ")


@client.command()
async def ec(ctx, am=1):
    await ctx.channel.purge(limit=am+1)


@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
   # await ctx.send("c  -> Clear Messages.\nw  -> Send text to emojis.\nwn -> "
   #                "Send text to emojis in a grid.\nwh -> Send text to emojis with no names.")
    embed = discord.Embed(title="Hi, I'm Emoji Wala :ghost:",
                          description="I can add some emotes to your messages and make them prettier !! :call_me:\n\n"
                                      "The current command prefix is  `~`\n ", color=0x00ffff)
    embed.add_field(name=":loudspeaker: Commands", value="` ec `  Clear recent messages.\n` ew `  Send text to emojis.\n` en "
                                                         "`  Send text to emojis in a grid.\n` eh `  Send text to "
                                                         "emotes without username.\n` er `  Add random emotes to text.", inline=False)
    embed.add_field(name="How To Use :question:", value="Example:\n```~ew Hey```**Result**:\n:regional_indicator_h: "
                                                        ":regional_indicator_e: :regional_indicator_y:\n\n```~er You Are Looking Good```**Result**:\n:nazar_amulet: You :sunflower: Are :cricket: Looking :notebook_with_decorative_cover: Good :skull:\n\n```~ec 10```**Result**:\nClears 10 recent messages.", inline=False)

    embed.add_field(name="\n:information_source: About", value="**Emoji Wala** is little fun project that adds some emotes to your text messages.\n This Bot is written in **Python** and is written by **[Arpit Mittal](https://discord.com/users/441622738533089321)**.\n\n**I hope you like it** :heart: :heart: ", inline=False)

    embed.set_thumbnail(url="https://raw.githubusercontent.com/ArpitMittal468/MyProjects/master/Discord%20Bot/png-transparent-ghost-emoji.png?token=AOSHJZ7HAPBQFPNVXQDRGDC64M226")

    await ctx.send(embed=embed)



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=":x: There is no such command.",
                              description=":white_check_mark: Use `~help` to get information.", color=0x00ffff)
        await ctx.send(embed=embed)


@client.command()
async def er(ctx, *, q=" "):
    #await ctx.send(q)
    await ctx.channel.purge(limit=1)
    q = q.strip()
    new_str = ''
    m = [':rolling_on_the_floor_laughing:', ':slightly_smiling_face:', ':hugging_face:', ':face_with_hand_over_mouth:', ':shushing_face:', ':neutral_face:', ':face_with_rolling_eyes:', ':lying_face:', ':drooling_face:', ':face_with_thermometer:', ':nauseated_face:', ':face_vomiting:', ':sneezing_face:', ':hot_face:', ':cold_face:', ':woozy_face:', ':dizzy_face:', ':exploding_head:', ':partying_face:', ':pleading_face:', ':tired_face:', ':yawning_face:', ':skull:', ':skull_and_crossbones:', ':clown_face:', ':ghost:', ':alien:', ':robot:', ':kissing_cat:', ':pouting_cat:', ':love_letter:', ':sparkling_heart:', ':revolving_hearts:', ':two_hearts:', ':orange_heart:', ':yellow_heart:', ':green_heart:', ':blue_heart:', ':purple_heart:', ':brown_heart:', ':dizzy:', ':hole:', ':bomb:', ':left_speech_bubble:', ':right_anger_bubble:', ':thought_balloon:', ':zzz:', ':raised_hand:', ':ok_hand:', ':sign_of_the_horns:', ':call_me_hand:', ':middle_finger:', ':selfie:', ':mechanical_arm:', ':mechanical_leg:', ':leg:', ':foot:', ':ear:', ':ear_with_hearing_aid:', ':nose:', ':brain:', ':tooth:', ':bone:', ':tongue:', ':baby:', ':child:', ':boy:', ':girl:', ':man:', ':woman_frowning:', ':person_pouting:', ':woman_gesturing_no:', ':woman_tipping_hand:', ':woman_facepalming:', ':woman_police_officer:', ':woman_detective:', ':woman_guard:', ':construction_worker:', ':woman_construction_worker:', ':prince:', ':princess:', ':woman_wearing_turban:', ':woman_with_headscarf:', ':pregnant_woman:', ':woman_superhero:', ':supervillain:', ':woman_fairy:', ':woman_vampire:', ':woman_genie:', ':woman_zombie:', ':woman_standing:', ':man_dancing:', ':woman_climbing:', ':horse_racing:', ':woman_biking:', ':woman_mountain_biking:', ':woman_cartwheeling:', ':women_wrestling:', ':woman_playing_handball:', ':woman_juggling:', ':woman_in_lotus_position:', ':couple_with_heart:', ':speaking_head:', ':bust_in_silhouette:', ':busts_in_silhouette:', ':footprints:', ':gorilla:', ':dog:', ':unicorn:', ':zebra:', ':deer:', ':llama:', ':giraffe:', ':elephant:', ':chipmunk:', ':hedgehog:', ':sloth:', ':otter:', ':skunk:', ':kangaroo:', ':dove:', ':eagle:', ':duck:', ':swan:', ':owl:', ':flamingo:', ':peacock:', ':parrot:', ':sauropod:', ':cricket:', ':spider:', ':spider_web:', ':scorpion:', ':mosquito:', ':microbe:', ':cherry_blossom:', ':rosette:', ':rose:', ':wilted_flower:', ':hibiscus:', ':sunflower:', ':blossom:', ':tulip:', ':seedling:', ':evergreen_tree:', ':deciduous_tree:', ':palm_tree:', ':cactus:', ':herb:', ':coconut:', ':potato:', ':carrot:', ':hot_pepper:', ':cucumber:', ':leafy_green:', ':broccoli:', ':garlic:', ':mushroom:', ':peanuts:', ':croissant:', ':baguette_bread:', ':pretzel:', ':bagel:', ':pancakes:', ':waffle:', ':cut_of_meat:', ':hot_dog:', ':sandwich:', ':taco:', ':burrito:', ':stuffed_flatbread:', ':falafel:', ':bowl_with_spoon:', ':popcorn:', ':butter:', ':salt:', ':dumpling:', ':fortune_cookie:', ':takeout_box:', ':crab:', ':squid:', ':glass_of_milk:', ':tumbler_glass:', ':cup_with_straw:', ':beverage_box:', ':mate:', ':spoon:', ':world_map:', ':compass:', ':mountain:', ':volcano:', ':wedding:', ':tokyo_tower:', ':statue_of_liberty:', ':church:', ':mosque:', ':shinto_shrine:', ':kaaba:', ':fountain:', ':cityscape:', ':sunrise_over_mountains:', ':sunrise:', ':bridge_at_night:', ':carousel_horse:', ':ferris_wheel:', ':roller_coaster:', ':circus_tent:', ':railway_car:', ':train:', ':metro:', ':light_rail:', ':station:', ':monorail:', ':mountain_railway:', ':ambulance:', ':fire_engine:', ':police_car:', ':oncoming_police_car:', ':taxi:', ':oncoming_taxi:', ':oncoming_automobile:', ':articulated_lorry:', ':motor_scooter:', ':manual_wheelchair:', ':motorized_wheelchair:', ':auto_rickshaw:', ':skateboard:', ':motorway:', ':railway_track:', ':oil_drum:', ':vertical_traffic_light:', ':stop_sign:', ':construction:', ':anchor:', ':sailboat:', ':canoe:', ':speedboat:', ':passenger_ship:', ':ferry:', ':ship:', ':airplane:', ':small_airplane:', ':airplane_departure:', ':parachute:', ':suspension_railway:', ':mountain_cableway:', ':aerial_tramway:', ':satellite:', ':rocket:', ':flying_saucer:', ':bellhop_bell:', ':luggage:', ':new_moon:', ':waxing_crescent_moon:', ':first_quarter_moon:', ':waxing_gibbous_moon:', ':full_moon:', ':waning_gibbous_moon:', ':last_quarter_moon:', ':waning_crescent_moon:', ':crescent_moon:', ':thermometer:', ':cloud_with_rain:', ':cloud_with_snow:', ':cloud_with_lightning:', ':fog:', ':cyclone:', ':rainbow:', ':closed_umbrella:', ':umbrella:', ':umbrella_on_ground:', ':snowman:', ':comet:', ':fire:', ':droplet:', ':christmas_tree:', ':fireworks:', ':sparkler:', ':firecracker:', ':sparkles:', ':balloon:', ':confetti_ball:', ':red_envelope:', ':reminder_ribbon:', ':admission_tickets:', ':ticket:', ':baseball:', ':rugby_football:', ':boxing_glove:', ':martial_arts_uniform:', ':goal_net:', ':ice_skate:', ':diving_mask:', ':sled:', ':curling_stone:', ':crystal_ball:', ':nazar_amulet:', ':video_game:', ':joystick:', ':slot_machine:', ':game_die:', ':teddy_bear:', ':flower_playing_cards:', ':performing_arts:', ':thread:', ':yarn:', ':sunglasses:', ':goggles:', ':lab_coat:', ':safety_vest:', ':necktie:', ':jeans:', ':scarf:', ':gloves:', ':coat:', ':socks:', ':dress:', ':kimono:', ':sari:', ':briefs:', ':shorts:', ':bikini:', ':purse:', ':hiking_boot:', ':ballet_shoes:', ':crown:', ':billed_cap:', ':prayer_beads:', ':loudspeaker:', ':postal_horn:', ':bell:', ':musical_score:', ':musical_note:', ':studio_microphone:', ':level_slider:', ':control_knobs:', ':microphone:', ':radio:', ':saxophone:', ':guitar:', ':musical_keyboard:', ':trumpet:', ':violin:', ':telephone:', ':telephone_receiver:', ':pager:', ':battery:', ':electric_plug:', ':desktop_computer:', ':printer:', ':keyboard:', ':trackball:', ':floppy_disk:', ':dvd:', ':abacus:', ':movie_camera:', ':film_frames:', ':film_projector:', ':camera:', ':camera_with_flash:', ':video_camera:', ':candle:', ':diya_lamp:', ':notebook_with_decorative_cover:', ':closed_book:', ':green_book:', ':blue_book:', ':orange_book:', ':books:', ':notebook:', ':ledger:', ':page_with_curl:', ':scroll:', ':page_facing_up:', ':newspaper:', ':bookmark_tabs:', ':label:', ':money_with_wings:', ':credit_card:', ':receipt:', ':envelope:', ':incoming_envelope:', ':envelope_with_arrow:', ':outbox_tray:', ':inbox_tray:', ':package:', ':postbox:', ':black_nib:', ':open_file_folder:', ':card_index_dividers:', ':calendar:', ':card_index:', ':bar_chart:', ':clipboard:', ':paperclip:', ':linked_paperclips:', ':scissors:', ':card_file_box:', ':file_cabinet:', ':wastebasket:', ':old_key:', ':hammer:', ':hammer_and_pick:', ':hammer_and_wrench:', ':dagger:', ':crossed_swords:', ':shield:', ':wrench:', ':nut_and_bolt:', ':gear:', ':link:', ':toolbox:', ':magnet:', ':alembic:', ':test_tube:', ':petri_dish:', ':dna:', ':microscope:', ':telescope:', ':syringe:', ':drop_of_blood:', ':pill:', ':adhesive_bandage:', ':stethoscope:', ':door:', ':couch_and_lamp:', ':chair:', ':toilet:', ':razor:', ':safety_pin:', ':broom:', ':basket:', ':roll_of_paper:', ':soap:', ':sponge:', ':fire_extinguisher:', ':shopping_cart:', ':coffin:', ':funeral_urn:', ':potable_water:', ':restroom:', ':baby_symbol:', ':passport_control:', ':customs:', ':baggage_claim:', ':left_luggage:', ':warning:', ':children_crossing:', ':no_entry:', ':no_bicycles:', ':no_smoking:', ':no_pedestrians:', ':no_mobile_phones:', ':radioactive:', ':biohazard:', ':place_of_worship:', ':atom_symbol:', ':star_of_david:', ':wheel_of_dharma:', ':orthodox_cross:', ':star_and_crescent:', ':peace_symbol:', ':menorah:', ':aries:', ':taurus:', ':gemini:', ':cancer:', ':capricorn:', ':aquarius:', ':pisces:', ':ophiuchus:', ':cinema:', ':vibration_mode:', ':mobile_phone_off:', ':female_sign:', ':male_sign:', ':infinity:', ':wavy_dash:', ':currency_exchange:', ':heavy_dollar_sign:', ':medical_symbol:', ':name_badge:', ':curly_loop:', ':part_alternation_mark:', ':copyright:', ':registered:', ':red_circle:', ':orange_circle:', ':yellow_circle:', ':green_circle:', ':blue_circle:', ':purple_circle:', ':brown_circle:', ':black_circle:', ':white_circle:', ':red_square:', ':orange_square:', ':yellow_square:', ':green_square:', ':blue_square:', ':purple_square:', ':brown_square:', ':black_large_square:', ':white_large_square:', ':black_medium_square:', ':white_medium_square:', ':black_small_square:', ':white_small_square:', ':large_orange_diamond:', ':large_blue_diamond:', ':small_orange_diamond:', ':small_blue_diamond:', ':radio_button:', ':white_square_button:', ':pirate_flag:']
    len_m = 515 - 1
    new_str = new_str + " " + m[randint(1, len_m)] + "  "
    for i in q:
        if i == " ":
            new_str = new_str + "  " + m[randint(1, len_m)] + "  "
        else: new_str = new_str + i
    new_str = new_str + "  " + m[randint(1, len_m)] + "  "
    #await ctx.send(new_str)

    i = 0
    cnt = 0
    old = 0
    while i < len(new_str):
        if cnt >= 1950:
            if new_str[i] == " ":
                await ctx.send("**" + new_str[old: i] + " **")
                old = i
                cnt = 0
        cnt += 1
        i += 1
    await ctx.send("**" + new_str[old: len(new_str)] + " **")


client.run(config.API_KEY)
