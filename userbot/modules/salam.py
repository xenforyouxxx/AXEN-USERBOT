from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Shalom Dulu Biar Sopan**")


@man_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HAI BAJINGAN, SHALOM!**")


@man_cmd(pattern="s(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**SHALOOOOMMMM...**")


@man_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**YE SHALOM.**")


@man_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**SHALOM DULU KATA YESUS**")


@man_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@man_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**HAIII PANTEEKKK SAYA {owner}**")
    sleep(2)
    await xx.edit("**LU SEMUA NGENTOTTTT 🔥**")


@man_cmd(pattern="y(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**NORAK GOBLOKK**")
    sleep(2)
    await xx.edit("**ALAY BANGET NGENTOT MAEN BOT MULU**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
