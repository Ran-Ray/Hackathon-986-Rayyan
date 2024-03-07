import discord
from discord.ext import commands
from model import get_class 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def waste(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file saved named {file_name}')
            result = get_class('keras_model.h5', 'labels.txt', file_name)
            if result[0] == 'Paper\n' and result[1] >= 0.6:
                await ctx.send('Paper Waste')
                await ctx.send('Paper accounts for 25 percent of waste in landfill and 33 percent of municipal waste. About 68 million trees are cut down each year to produce paper and paper products.')
                await ctx.send('Here is how recycle paper waste:\nStep 1: Separating\nIt all starts at your home by sorting paper waste, such as old newspapers and paperboard boxes, from other recyclables and garbage. We recommend using a designated paper recycling bin for the collection of your paper waste.\nKeep paper that you recycle as clean as possible by collecting it in separate bins from all the other recyclable materials. This is the best way to ensure that the waste paper can be recycled properly.\nStep 2: Collecting\nThe local waste hauler collects the old paper from centralized drop-off containers in your area or the curbside collection or picks up containers that get emptied on scheduled moments. The material is then getting transferred to a recycling center or a materials recovery facility (MRF).\nStep 3: Sorting\nAt the recycling facility, the actual recycling process starts by sorting and separating the mix of paper waste into multiple grades that contain different types of paper, such as newspapers, cardboard boxes, printer paper, magazines, and mail. The facility roughly sorts the paper waste into two streams: pure paper waste and pure cardboard waste.\nDuring this process, contaminations are also getting removed from the paper, such as plastic, wood, or other foreign materials. The sortation process is partially done by machine but also by hand.\nStep 4: Baling\nThe sorted paper waste gets baled into paper bales for further transport. Not every recycling center bales the waste paper. Some opt to deposit the material in large containers to be transported to the paper mill.' )
                await ctx.send('Step 5: Pulping\nAt the paper mill, the actual papermaking process starts. Here the paper is put into a large machine mixed with water and chemicals that converts the paper into paper pulp.\nThe mixtures help to break the paper down. This process is called pulping and is meant to mix all the paper and clean the material from impurities.\nInk (de-inking), metals, glass, plastic, adhesives, and other contaminants are removed from the paper pulp during the process. This results in a homogeneous mix that looks like a grey mixture that forms the new papers base.\nIn the process of pulping also virgin wood fibers are added to the mix to ensure the materials strength. This means that waste paper is a secondary resource for papermaking.\nStep 6: Drying\nNow the clean pulp is ready to dry. The process works by pressing the material between large rollers to drain and extract the pulp’s water. The drained pulp is now spread out and passed through heated metal rollers that dry the paper entirely.\nStep 7: Rolling\nDryers now treat the dried and flattened fresh paper layers to smooth out the paper from any wrinkles. Finally, the paper is being rolled onto massive metal rollers, where the material is then getting rated by quality controllers that check the strength and the grade of the paper.\nStep 8: Selling\nThe paper rolls can now be sold and shipped to other manufactures that use the freshly recycled paper for new products, like newspapers, magazines, or postcards.')
            elif result[0] == 'Plastic\n' and result[1] >= 0.6:
                await ctx.send('Plastic Waste')
                await ctx.send('Humans currently produce more than 350 million metric tons of plastic waste per year.')
                await ctx.send('Here is a few idea to recycle your plastic waste :\n1.Reuse Your Plastic Coffee Creamer Containers for Snack Storage\n2.Make a Plastic Bottle Planter\n3.Start a Herb Garden With Empty 2-Liter Bottles\n4.Make a Beach Bucket From Laundry Detergent Containers\n5.Reuse Soda Bottles by Creating a Vertical Garden\n6.Reuse Plastic Bottles to Make a DIY Sprinkler\n7.Create a Piggy Bank Made From a Reused Plastic Bottle')
            elif result[0] == 'Household waste\n' and result[1] >= 0.6:
                await ctx.send('Household Waste')
                await ctx.send('We throw out over 2 billion tons of household waste a year globally. That’s more than 60 tons of waste every second.')
                await ctx.send('Here is how to compost your household food waste:\nSetup\n\n1.Drill some ¼ “ holes in the top, bottom, and sides of your 5-gallon bucket. These are needed for aeration.\n2.Add a layer of browns, about ¼ of the total volume.\n3.Add a layer of greens, then browns, in a 1:1 ratio. Continue to add layers until the bucket is about ¾ full. The base layer of browns should make the overall balance favor browns, which will help cut down on odor and pests.\nMaintenance\n>Add greens/browns to the compost. Make sure to avoid adding the materials listed in the above “Do not add” section, and keep the ratio as close to 1:1 as you can while minimizing smells and pests.\n>Aerate it once a week. Either roll the sealed bucket on the ground while it is light enough or use a tool to mix the insides around.\n>Add moisture as needed - the compost should feel like a damp sponge, but not leak water when squeezed\n>Add browns as needed - if odor, pests, or overwatering becomes an issue, dry browns will keep them under control\n>Cold temperatures will slow your compost - try to keep your container in a slightly insulated area\nTip: chopping up your greens and browns before adding them speeds up the compost ')

@bot.command()
async def plant(ctx):
    await ctx.send('How  to  plant:\nStep 1: Choose Your Seeds\nStep 2: Gather Your Equipment(A seed-starting tray or small pots,Seed starting mix or potting soil,Watering can or spray bottle,Labels to identify your plants,A sunny location or grow lights)\nStep 3: Prepare the Soil\nStep 4: Sow Your Seeds\nStep 5: Provide Proper Care\nStep 6: Transplant Your Seedlings after your seedlings have grown a few inches tall')
    await ctx.send('you may encounter some potential problems. These include:\nOver or under-watering: If your plants are wilting or turning yellow, they may get too much or too little water. Adjust your watering schedule accordingly.\nPest infestation: Look for signs of pests, such as chewed leaves or tiny holes in the leaves. Treat with an organic insecticide if necessary.\nDisease: If your plants are showing signs of disease, such as spots or discolouration, remove them from the garden to prevent the spread of disease to other plants.')

bot.run("Token")
