def solve_array_problems():
    # Ma'lumotlarni kiritish
    n = int(input("N ni kiriting: "))
    a = []
    print(f"{n} ta elementni kiriting:")
    for _ in range(n):
        a.append(float(input()))

    # Array21, 22, 23 uchun K va L ni kiritish
    k = int(input("K indeksni kiriting (0 <= K): "))
    l = int(input("L indeksni kiriting (K <= L < N): "))

    # --- Array21: K va L orasidagilarning o'rta arifmetigi ---
    sub_array = a[k : l + 1]
    avg_kl = sum(sub_array) / len(sub_array)
    print(f"\nArray21: K va L orasidagi o'rta arifmetik: {avg_kl}")

    # --- Array22: K va L dan tashqaridagilar yig'indisi ---
    outside_elements = a[:k] + a[l + 1:]
    sum_outside = sum(outside_elements)
    print(f"Array22: K va L dan tashqaridagi elementlar yig'indisi: {sum_outside}")

    # --- Array23: K va L dan tashqaridagilar o'rta arifmetigi ---
    if len(outside_elements) > 0:
        avg_outside = sum(outside_elements) / len(outside_elements)
        print(f"Array23: K va L dan tashqaridagi o'rta arifmetik: {avg_outside}")
    else:
        print("Array23: Tashqarida elementlar yo'q")

    # --- Array24: Arifmetik progressiya ---
    is_arifmetika = True
    if n >= 2:
        d = a[1] - a[0]
        for i in range(2, n):
            if a[i] - a[i-1] != d:
                is_arifmetika = False
                break
        print(f"Array24: {'Ayirma ' + str(d) if is_arifmetika else 0}")
    else:
        print("Array24: 0 (elementlar yetarli emas)")

    # --- Array25: Geometrik progressiya ---
    is_geometriya = True
    if n >= 2 and a[0] != 0:
        q = a[1] / a[0]
        for i in range(2, n):
            if a[i-1] == 0 or a[i] / a[i-1] != q:
                is_geometriya = False
                break
        print(f"Array25: {'Maxraj ' + str(q) if is_geometriya else 0}")
    else:
        print("Array25: 0")

# Dasturni ishga tushirish
if __name__ == "__main__":
    solve_array_problems()
