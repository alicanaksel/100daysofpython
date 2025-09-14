log={
    "France":{
        "cities":["Paris","Nice",["Monaco"]],
        "total visits": 12
    },
    "Germany": {"cities":["Berlin","Hamburg"],
                "teams":{"bayern":["Munich","Leverkusen"]}}
}

print(log["France"]["cities"][1])

print(log["Germany"]["teams"]["bayern"][1])