d1={}
print(type(d1))

d2={"DM":"BS", "BCT":"RSG", "IOT":"MKP", "MOSA":"RM", "CC":"SGP"}
print(d2)
print(d2["IOT"])
print(d2.get("IOT"))

d2["FA"]="CT"
print(d2)

d2.update({"PC":"AT"})
print(d2)

print(d2.keys())
print(d2.items())