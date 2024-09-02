# შექმენით სკრიპტი ლოგიკური ოპერაციების შესასრულებლად (და, ან, არა).
try:
    value = int("abc")#Error: can't convert
except ValueError as e:
    print("Error:", e)#Print error message
