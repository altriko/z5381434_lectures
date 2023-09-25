# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs_2 = set()
for i in f_suburbs:
    if i[0] == "F":
        f_suburbs_2.add(i)
    else: pass

new_set = {"Fairfield","Fairfield East","Fairfield Heights","Fairfield West","Fairlight","Fiddletown","Five Dock","Flemington","Forest Glen","Forest Lodge","Forestville","Freemans Reach","Frenchs Forest","Freshwater"}
f_suburbs_2.update(new_set)

f_suburbs = f_suburbs_2
print(f_suburbs)

