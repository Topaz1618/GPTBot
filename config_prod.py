"""
Author: Hang Yan
Date created: 2023/8/13
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

HISTORY_SIZE = 30


prompt_settings = {
    "Language": {
        "prompt": "You are a language learning assistant robot.",
        "desc": ""
    },

    "Dating": {
        "v1": {
            "prompt": "You are a partner robot.",
            "desc": ""
        },
        "v2": {
            "prompt": "You are a partner robot.",
            "desc": ""
        },

        "v3": {
            "prompt": "You are a partner robot.",
            "desc": ""
        }

    },

    "Interview": {
        "prompt": "You are a interview robot.",
        "desc": "",
        # Usage: f"{a['prompt'].format(title='Python Developer' ,tech_stack='Python, AWS')}",
    },

    "Prompt": {
        "prompt": "You are a prompt robot. ",
        "desc": "",
    }
}
