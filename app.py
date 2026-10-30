from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

CASES = [
    {
        "id": 1, "title": "The Missing Backpack", "level": "LEVEL 1", "emoji": "🎒",
        "scene": "park.svg",
        "story": "Oh no! Mia's backpack has disappeared from the park bench. The security camera found a clue, but the computer program has a tiny bug. Can you fix it?",
        "clues": ["🪑 The backpack was last seen beside the blue bench.", "📹 The camera says backpack_found is False.", "🕵️ The program should print that the backpack is missing."],
        "lesson": "In Python, = stores a value. == checks whether two values are equal.",
        "starter": "backpack_found = False\n\nif backpack_found == True:\n    print('Backpack is safe!')\nelse:\n    print('Backpack is missing!')",
        "broken": "backpack_found = False\n\nif backpack_found = True:\n    print('Backpack is safe!')\nelse:\n    print('Backpack is missing!')",
        "answer": "backpack_found = False\n\nif backpack_found == True:\n    print('Backpack is safe!')\nelse:\n    print('Backpack is missing!')",
        "output": "Backpack is missing!", "suspect": "The backpack is still missing!",
        "explain": "Great debugging! You changed the single = into ==. Python can now compare the value and follow the correct path."
    },
    {
        "id": 2, "title": "The Library Password", "level": "LEVEL 2", "emoji": "📚",
        "scene": "library.svg",
        "story": "A secret note is locked inside the library computer. The password is stored in a list, but the program is looking in the wrong place. Help the detective find it!",
        "clues": ["🔐 The password list starts counting at zero.", "📖 The secret word is the second item.", "💡 Python lists use square brackets to pick an item."],
        "lesson": "List positions are called indexes. The first item is at index 0, the second at index 1.",
        "starter": "passwords = ['apple', 'puzzle', 'star']\nsecret = passwords[1]\nprint('Password:', secret)",
        "broken": "passwords = ['apple', 'puzzle', 'star']\nsecret = passwords[3]\nprint('Password:', secret)",
        "answer": "passwords = ['apple', 'puzzle', 'star']\nsecret = passwords[1]\nprint('Password:', secret)",
        "output": "Password: puzzle", "suspect": "The password is PUZZLE!",
        "explain": "You fixed the list index! The second item lives at position 1 because Python starts counting from zero."
    },
    {
        "id": 3, "title": "The Café Mystery", "level": "LEVEL 3", "emoji": "☕",
        "scene": "cafe.svg",
        "story": "The café's special recipe has vanished from the menu. A tiny loop should read every ingredient, but it stops too early. Fix the loop and reveal the recipe!",
        "clues": ["🥛 Ingredients: milk, cocoa, sugar.", "🧾 The program should print all three ingredients.", "🔁 A loop repeats an action for every item."],
        "lesson": "A for loop visits each item in a list, one at a time.",
        "starter": "ingredients = ['milk', 'cocoa', 'sugar']\n\nfor item in ingredients:\n    print(item)",
        "broken": "ingredients = ['milk', 'cocoa', 'sugar']\n\nfor item in ingredient:\n    print(item)",
        "answer": "ingredients = ['milk', 'cocoa', 'sugar']\n\nfor item in ingredients:\n    print(item)",
        "output": "milk\ncocoa\nsugar", "suspect": "Mystery recipe found: CHOCOLATE MAGIC!",
        "explain": "You spotted the typo! The list is called ingredients, and the loop now visits every item."
    },
    {
        "id": 4, "title": "The Kite Shop Mix-Up", "level": "LEVEL 4", "emoji": "🪁",
        "scene": "kite.svg",
        "story": "The kite shop is choosing the wrong prize color. A tiny check is comparing the wrong value. Fix the operator so the correct kite can fly!",
        "clues": ["🎐 The lucky color is yellow.", "🚩 We want to know if the color is not yellow.", "💡 Use != to mean 'does not equal'."],
        "lesson": "Use != when you want to check that two values are different.",
        "starter": "favorite_color = 'blue'\nif favorite_color != 'yellow':\n    print('The kite is ready to fly!')\nelse:\n    print('This color is not the winner.')",
        "broken": "favorite_color = 'blue'\nif favorite_color = 'yellow':\n    print('The kite is ready to fly!')\nelse:\n    print('This color is not the winner.')",
        "answer": "favorite_color = 'blue'\nif favorite_color != 'yellow':\n    print('The kite is ready to fly!')\nelse:\n    print('This color is not the winner.')",
        "output": "The kite is ready to fly!", "suspect": "The blue kite wins the race!",
        "explain": "You used the not-equal check correctly. Now Python compares the color the right way and picks the winner."
    },
    {
        "id": 5, "title": "The Birthday Box", "level": "LEVEL 5", "emoji": "🎁",
        "scene": "gift.svg",
        "story": "The party planner is packing a birthday box, but one tiny symbol is stopping the final gift from being added. Can you fix the surprise?",
        "clues": ["🎉 The box needs both items to match.", "📦 Each item is a string value.", "✅ The code should use and to combine checks."],
        "lesson": "The and operator makes both conditions true at the same time.",
        "starter": "gift1 = 'book'\ngift2 = 'pencil'\nif gift1 == 'book' and gift2 == 'pencil':\n    print('Birthday box is perfect!')\nelse:\n    print('The box needs a fix!')",
        "broken": "gift1 = 'book'\ngift2 = 'pencil'\nif gift1 == 'book' and gift2 = 'pencil':\n    print('Birthday box is perfect!')\nelse:\n    print('The box needs a fix!')",
        "answer": "gift1 = 'book'\ngift2 = 'pencil'\nif gift1 == 'book' and gift2 == 'pencil':\n    print('Birthday box is perfect!')\nelse:\n    print('The box needs a fix!')",
        "output": "Birthday box is perfect!", "suspect": "The birthday box is perfect!",
        "explain": "You fixed the comparison inside the and condition. Now both gifts match, so the surprise is ready."
    },
    {
        "id": 6, "title": "The Picnic Basket Count", "level": "LEVEL 6", "emoji": "🥪",
        "scene": "picnic.svg",
        "story": "The picnic basket is nearly packed, but the helper forgot to count the snacks correctly. Fix the code to reveal how many treats are inside!",
        "clues": ["🍎 The basket has three snacks.", "🔢 Use len() to count how many items are in a list.", "📋 The answer should be the total number of snacks."],
        "lesson": "len() tells you how many items are in a list.",
        "starter": "snacks = ['apple', 'banana', 'cookie']\nprint(len(snacks))",
        "broken": "snacks = ['apple', 'banana', 'cookie']\nprint(len(snacks)",
        "answer": "snacks = ['apple', 'banana', 'cookie']\nprint(len(snacks))",
        "output": "3", "suspect": "The basket has 3 snack treats!",
        "explain": "Great catch! You closed the parentheses, and the code can now count every snack in the basket."
    },
    {
        "id": 7, "title": "The Garden Gate", "level": "LEVEL 7", "emoji": "🌼",
        "scene": "garden.svg",
        "story": "The garden gate only opens when the right flower is checked. A tiny membership test is missing, and the gate won't budge!",
        "clues": ["🌻 Daisy is one of the flowers in the garden.", "🔎 We are checking whether a value is inside a list.", "💡 Use the in keyword for membership tests."],
        "lesson": "The in operator checks whether a value appears inside a list.",
        "starter": "flowers = ['rose', 'daisy', 'tulip']\nif 'daisy' in flowers:\n    print('Daisy is in the garden!')\nelse:\n    print('No flower found.')",
        "broken": "flowers = ['rose', 'daisy', 'tulip']\nif 'daisy' == flowers:\n    print('Daisy is in the garden!')\nelse:\n    print('No flower found.')",
        "answer": "flowers = ['rose', 'daisy', 'tulip']\nif 'daisy' in flowers:\n    print('Daisy is in the garden!')\nelse:\n    print('No flower found.')",
        "output": "Daisy is in the garden!", "suspect": "The garden gate opens for Daisy!",
        "explain": "You used the membership check correctly. The in operator asks whether a value is inside the list, which is exactly what we need here."
    },
    {
        "id": 8, "title": "The Starry Treasure Map", "level": "LEVEL 8", "emoji": "⭐",
        "scene": "stars.svg",
        "story": "The night sky treasure map is glowing, but the code is shouting in lowercase. Fix the loop so each star name shines bright and proud!",
        "clues": ["✨ Each star name should be written in uppercase.", "🔁 A loop checks each item in the list.", "📌 Use .upper() to change text to uppercase."],
        "lesson": "The .upper() method turns lowercase text into uppercase text.",
        "starter": "stars = ['sparkle', 'glow', 'twinkle']\nfor star in stars:\n    print(star.upper())",
        "broken": "stars = ['sparkle', 'glow', 'twinkle']\nfor star in starz:\n    print(star.upper())",
        "answer": "stars = ['sparkle', 'glow', 'twinkle']\nfor star in stars:\n    print(star.upper())",
        "output": "SPARKLE\nGLOW\nTWINKLE", "suspect": "The treasure map glows with SPARKLE, GLOW, and TWINKLE!",
        "explain": "Perfect fix! The loop is now reading the correct list, and each star name becomes uppercase so the map shines clearly."
    }
]

@app.route("/")
def home():
    return render_template("index.html", cases=CASES)

@app.get("/api/case/<int:case_id>")
def get_case(case_id):
    case = next((c for c in CASES if c["id"] == case_id), None)
    if not case: return jsonify({"error": "Case not found"}), 404
    return jsonify({k:v for k,v in case.items() if k not in ("answer", "output", "suspect", "explain")})

@app.post("/api/check")
def check():
    data = request.get_json(force=True)
    case = next((c for c in CASES if c["id"] == int(data.get("case_id", 0))), None)
    if not case: return jsonify({"success": False, "message": "Case not found"}), 404
    submitted = data.get("code", "").strip().replace("\r\n", "\n")
    expected = case["answer"].strip()
    # Safe classroom game: compare the repaired text; never execute user-submitted code.
    if submitted == expected:
        return jsonify({"success": True, "output": case["output"], "suspect": case["suspect"], "explain": case["explain"]})
    return jsonify({"success": False, "message": "Not quite yet! Check the highlighted clue and try again."})

@app.get("/api/hint/<int:case_id>")
def get_hint(case_id):
    case = next((c for c in CASES if c["id"] == case_id), None)
    if not case: return jsonify({"hint": "No hint found."}), 404
    return jsonify({"hint": case["lesson"]})

if __name__ == "__main__":
    app.run(debug=True)
