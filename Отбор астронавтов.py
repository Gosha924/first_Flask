from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/index')
def countdown():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def advetisment():
    data = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!', 'Присоединяйся! ']
    return '<br>'.join(data)


@app.route('/image_mars')
def get_mars():
    return f'''<title>Привет, Марс!</title>
                <h1>Жди нас, Марс!</h1>
                 <img src=data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgWFRYZGRgZGRocGRocHBoaGhoaGRgZGhgaGhgcIS4lHB4rIRgYJjgmKy8xNTU1GiQ7QDszPy40NTEBDAwMEA8QHxISHjYrJCs3NDQ0NjQ0NDQ0NDQ0NDQ0NDY0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAFBgMEAAIHAQj/xAA/EAACAQIFAQUGAwYEBgMAAAABAhEAAwQFEiExQQYiUWFxEzKBkaGxFELBB1Jy0eHwFjNishUkgpKiwiM08f/EABoBAAMBAQEBAAAAAAAAAAAAAAECAwQABQb/xAAtEQACAgEEAgAFAgcBAAAAAAAAAQIRAwQSITFBURMyYXGBIrEUM0JSkaHRBf/aAAwDAQACEQMRAD8A5MEPMVsU8a9W8YjpUloTzWhIRkYSpsNaBPeMCpHwjhdWlgp4MGPnUSrTUKbX0UHu7it7dgFC0iR0616qdBvV+xlrMODNEVsHJamvRbIo5mGQXbKI7oVDzpmN4iduRz1oWpgyaNATsJ5Zn9yxZuWVVStwQxI3Hoa0yzIr19HuW1lLYljPFUHeTNWMNiriBlR2UN7wBIB9R1rqCQWcOWYKOSYqzmmVPYYI4gkA/A1FbDAyOR1oljcLd0LduGVbgkyaNAsF4Z9BmAdutRsJ3q/g8I11giKWYnYDmmG92NCKPaYhEYidMFvqDv8ACi1StjQhKbqKt/QT0tE049iuy5vOHuKdA+tBbmWvbdQSrKT7yGVPGx6g78ECuzYG2LdpFAHujjjiuTSVonkjNS2NV7LVpURQiKABsBXlzDW35UfDb7VRiTzV22hArHOUk7TNkMcaqjnPb3swE76Lsev6GkSyqAEMN6+gMxw3tLDp1KmPUcVwXE2x7SG2GqG+e9Wxz3RtkZx2yo8XEJoIZZfoaGladsw7P2bSnvghlDKZnmlS/hNI1Agg0/a4E6YR7P5ZYuo/tbqoy+6DydulDUyx3ZxbUuEEsR0XxqtEUQwyXbQ1gugdSJEgOp536iiu+Tndcdgl1r22N6kupBqM0owYwV4AQTWuPuAih2GZdY1khZ3jmK8xJGohZKztQOojmsq1+GT96soBKASpEEUSyLL/AGrgGmXOuzAtpqXmj0Ldi/fzl2siyQAoMz1qvj7doBDbcsSvfBHDeVV75JNaqKZAZcwDhTJpxwuJAAZDpI6gwRSOrGp7V1o5MUaOHvH5wcSNL7wBt0kD3h5kz86U80w2lthRLKryad9jWmaMpGx3rkKkl0AgnjzXqEipDaM7ii2VZFcvMAqE+lUUWxXJLsG2A24A5ovgcnxN/Sihio4n3V85PFP2X9nMPhk13od493oPHfqRVfHdpiGCWrXTUpHdSIlYH5gR8OOaWU4x6Vl8ODJl56Rcy3IbeFtbMgc++7Hw6DwE/Ok3O7ia9akXo2l2AQTsAqD8vO5JJ60yYHAX8STcuk6FU6bYkamnYz+bjw68UPzvshdUTbl5JOkDbaIjw5PyFZss5yVUexo44sUqk/8AgOsX5T2mlN9RgRAKmNMbGYKn0PXoxZXmrusal0iApaZkwAJA087bnoaA5L2UxDo7MGWNkSIJO41bwI3MfHjrthsqv4c67iQqNJ3gsFIBI1QOWUDx+BrEviRdm/LHT5U4tptdBy8cSryIYBoMEHiCeD50y4LEFlE80m4zNmtOhClA6htDHusCN9p4G/SdwesUXwObBwrIGUlZKlYB3KkpvvxMeB+FGWS+zFLSSUU10MePxASy7kxCn7bVwLEEliTvud6f+1uMxLWyJDW530iPTVB259KRTaaJgxW3Ako37PK1EXGVNHmKzC5cCK7EqggbDYfrXmapZV/+XZ2SBu4hpjefjUZSo2SrVRnIGWanW4SgDOSEkIhJIAJk6RwN61W0WIAEk8CvdCgMGB1fbxrmjrIbuHYAMRseKhC1ZYOVEzpHHhUDLQCiy9uz7EEMfa6jKxtp6Qahw99VBBWSePKoiKjalCiT2vlXlR1lcELZO7oda9N6Z7ebfiWW07hAdix4G1JVgt7oJ36VfGFdACRtRqxTM0wvs3ZAwcA7MODQ8CrF+4W5qNNiD4ePFFHMxNqvvilKBFRRvOr8xmNifD+dVWfU5ZokkkwABv4AbAVsF32ooVlq0pjafhW1pyGBO9Xctzc2kZERe8IJMk9d/rVjJMra84AHJqqjZFzcbb6CWSZScQ5dwFRRqZjwAKfHVrSBcPbjYc8jYTMcnn41bw2BTDWgm07FvMjgfChmPzc+6OKVyvrofDw9zXP7G+Bw3dJvkF3mV22HQE+PnRrCBHUhUEIAAIHTgCk1b5Jk77/D5U0dncWqIVbYk7eYI2qGR8WalJtllMRG3FSJiZPlVQqCzRwTIrdEAgVicmXSQQD9KkMHZgDxyJ3BkVBbPSpgKVyYTTGYG1dUrcVWB6ED70Mzrs6t22FQ6CsFOgWAQAI4G/2o0KwNXbr7GhknBpp9CHjcqa1ZV7hfWTDLp1yDzLcHbUSesgdKE5ndtew02wCh52EqeDvsYnxA5FdVMEQdxS7jezgVy9oSjAhrZCkQeSoPqfn1poScZXH8o0PLDPFxy8Pmn4+xxS4m9QlaYu0WT+xeB7jbqfDxX1B/ShWJwDpBdGWRIkRINejFqStHlTg4SaZRZCN/rUR6+dXHunTp6TNV2FEQsrjgLWjSPWhbCp2FaMm00AkBFe2LQYwalX61EwINKEk/BedeVHJ8aygEt5PdVLiluJp47SZzhriDQgQ6YMRufGucqaJWMC7pqG4FFqxemVWO9TOywPGoNJr0UyAShRFT2LrqrBTswg7Dcc1XUVPbNOkLIsYOwWYAda652VywYaz7RveI7v6mk3sTlXtLqkjYGT5Abmn7OL8jSvAEDyppf2++zNe6V+F+4GzTMmdjB2oW7E81YxNvRG/O8+tUHxQ4J8aEnGKNMIthXAYqygfWJJXu+VQJmmnk7R/f9+VKuPzdVnSwLA+7ztwYPiOYPlQTE5hefqUjfY9Rx9/tWGeSzZDFR0g9oEVgARuTA+Gr+dbP2iUAnYw0HePIj1/mK5e2Vl0DNcbV4Sfnv16Vp/wslT/8h35GoknaNx/Os7cS6izreG7TIZXUCQd4I22kT8BNG8NniEcgbePnFcGGW3EHcaJMkjkx0LeHlREYzEu6ksdKlToUmJETE8cfD5yHQVBs7tbzBSYmiSgFZrjGBz+4kB1gQe9uT1KiDztAmfOmnJ+1gcAb7SCODtG8TS1QJY2PgNbq0VQweOVwIq7QTJtUL/a3IhetMyjvDvR5gcj14Nc2uZmXOjFM7qiFU06QwYe7JPIrtdp+lct7d5F7G6XQdx+8PLxFbtPNSW0llbaV+P2EZxUboIqyU33qG4sGtLM5WZa1cRU4QkgDrUuPwbIBqigcDetW8uyx8Q+lBJAk+QrfLVt61N2SgPeA5irj5oLF9nwpITgAjkHkEGld+Arssf4Rf96srP8AFl7xX5VldZ3IrAVYt32AgMQPCoYrcUUcTPdJAEcVqFrLXNPIsYA5dMxieZ/Nq1cfwxTdcg80KuHyu69tryoSiGGYcD1rzC29TAVLhs0uoj20dlR/fUcGruQYYvcUeJFUirZHI9sWzpPZfCizhy0d5th6Dc/35VmJuRJaimIQIgXoigfLn6zSnm2PLd2e6sxS7u5CYYN0gfjsXO5Owpdx+Yh0Cp7xbc+Q2gevM1DneY629mh2HvEePhUeDtAb1inkcn9D1YY1FWZh8EBzVlcKPD+/KovxLPtbXb948fAdaktJc6v9BUpMtFWT2stBMmfjVuzlRY7AAVNhHPXejGGaoyLRRHh8htwNUt6kx8hV9MvRfdQD0Aqzbry8DG21SY6RTu5ajdBQXHZCyHXbJBHhRR7F2ZW6fQhSPtWyYy6n+ampOrpuR5lPD0oqTQdq8AnKu0b2m03AZ4kfyn0rouUZwLgE0j5/k6XLftLcEESCOoof2XzjS3s3J1r1/eHHz4ornklOCaOxL4ihfazAi7h227yd4fr/AH5VYybF61G+9X3TUjr4gj5ir4ntkmYsi8HAcYkE1Rei+b2tLsPM1BcytvYi9K6S2mJGqRztyK9NmUt9krOGa9GJbSunuHgavM9K97Q2ULNoeVB7vpQKrGEte0bSbioY7uqYZiQAs8LzMnbakfs4FOIrRqJXcAwdlO5UkGNxt4EcitsDl2twjbTXNhQKispt/wAMp+99q9oWjhZbBmreX5T7RHZWGpBOk8sN5g+O1PjYNCIKiPSkfOsOEdgvFLGV8ILjXZeyHBYJ7N44i6UuKD7MTE7bQPzGdopfrVRUgFW7J1Rui0+fs+wGq7rI2QaviOPrFD+xeLwyC4MQslxC7AiPXoaeOz+HSxh3dfzHb0H/AO0d1JohkW6l9TfPsV+Rdz19aQO0eO9ipLCG4UGdz0FH8ViyGLk8GZ8IrmnavtAcXf16YVRpTwO+7fHwrLmn/TH8m7Bj2q2Q5bLMWPJJJ9SZNHksahp6dfMeFBcpWmFDCyBUFwrNffBK7Ii7kCqoxiEwrA1RtZddxV0qG0Iol3Oyqo5JPhsflUV7D4JdrX4m4OPa6rdtWI6qjKSR6waCxylyGWWMOGMGHvUcwTzSpg1ZToaZiQWUoxX/AFIeGHXkbggkGmbKxNJKLS5KQmn0H7Ar28YFTYW1tVXO30IWJC9NRkgT1gbnyA5MDrWd23SLWlywRjM2RDBYT4VPlWf23aNQNKFzM8Lq0th3uEncviAjmeoRUKqfKT69alx/Z5BbGNwTt7NXC3kf/MsNt725ldwZk7GZjiz08lG2RjqYOW1HSreCUK2j3H3joG6keR+/rXLe0aNh7+tdoO/mOtdN7K3me0A/I/s8Ul/tRw+khvFT96jDui0uLsbOxmaBwpB5j610Beh8a4F+zfMDuh5U7eh6feu7Zfc1IDWiPEqMWVWlI4/2sw+nEOPBj96W3NM3a19WIuR+8fvS04r1F0YX2QMKkwyKSdZjbbzNasKKdmMJauYhEvGEPwk9N6WTpWcuS/lCoyRIB86H55CnumCPCjHbrC2cO6JYGk6ZaDzuYNJ1y4znqaWvJyd9Ev41/wB4/OsqH8M/7prKAR6uZqgWdQpJzLFa3LVR9ofGtiRA8etGMaC5Wep41IBXsppXTq1b6pjT5QOas4xrfd9mGHdGrVHv/miOlVRNm+X2dTgeddWzMhMPatj92fnvXOOzag3UB8RXRu0PvhfBV+1LmltihMcd+WvSObdtMx0qthT3rnveSzuPidvgaVEee6FEelb9pcSXxdxj+R9I8gu33n51FYMT8x5g157TpP2etjaba9cBPLlho86ZcPakRSplby3yP1inXAOBBqkeYnNPdSIlw3/LYi2m7urccsBHdHmVGn40k57ltwOHVWe2yjSygsAABIMe6ZnbzrreHSw5lkE+IkfajWFwtvpPxJNL8eKW1oWWlk2pJ+zlnZXB3rzs90u5SyQWYkwS9tUQseunWY8qc8qwpBg02uEVY4A6UnNnCC6xB7oYr8QYNSlk3N0iuLE0qHXBYPal3t3g2NlQu3f7x6AFHAJ8tRX5iieV57bMAN8DxRjEXFYAzzUYtRkn6DlhOnF9M+Yr+W3lcqUYmeQCQT4g9a7D2EJK4j2x1B7Vq24513AjghY95oJJP+oGnA2FPOk+oBqzYsovAUegA+1aHqFTSX+zP/DNNNvr0QZRlwtW0XqFUH1A3pN/arhgbdsniSD/AOJ/Suge1Fc7/a1cJXDoOpdj/wBOgD/c3yrL07NmJOc0n5Erspc04lQOG2rvmRnuVwLsxZLYlI/KJNd6yUwsGqQfKO1kUuEclz9WF5w3Ooz86D3EpqzYLdxDt0Lt96uvkqaAxAgiQfTY16+5JI8ZrkQWWo9RBkGCOtEcfhwpMHih7CuZxYxGIV0l9ReeSZ2qpbfSZFYRWpFKcXP+It4V5VOKyhRxSq/lGXNfuLbUgE9TxVILU2GdlYFSQekUyOd1wXs1yw4e4bbEMR1HBqmBvW+Ldy3fmfPmo1pogYcyF1W4pJ610rO0l1YcMikfKuSYR4YV1bLroxOGXQZe0OOpU0meO6P2Biltyfc4l2ywPs8SxiA/eHqfe+u/xobhLk90mP3SfHw9DXU+0eWJfXcbiuf5h2dZfc38qzKLqjW5VK0TYLCaCHPP86Zg8CkJrl5BBLACmXIMwFy3pY99RB8WX8rfofh41yTVplo5E2vYew2NIPNMWBzIxzSgF3oxld0Awax5I8noKSoJZhnwMoDv18qDYbJrdxpZiN9XofEVDnmWBnZ0JUtwy9DEb+IpWfC4gMQym4B5kfEHimiqiT7fF/g6rg+yuGZQGLMymVeYZT5EUYzi+tm0NJ2UbbydvOuN2FxTELZw91W8S77fHuwKcMt7PYp0JxeIZhHdRTI/6mO59PvU3H6oZ2+Xf5VF/DdpdXWitjNietJTZfoaiGGvaanKNdFoOL8Dph8ZPWhvazC27q63aCinedhO5n6VTtZiltGuOYRBJPU+CgdWJ2A8TS3lXY/E4+5cv4o3LKXHDhD+ZSQQInYBQBuJ2FGEHLt0TyZIwkmlyE/2eZPrLXiuxPdJG5A45ro+aYn2WGdxsQsD1O3863y3LktIqIIVRApe7f48BFtA7+83yhf1rVgjc0efny7k2xFTFQ01dOfuqMgIKt0ImD4r4HpQVqjavSaTPPss4FEuXQLr6EMkt6AkD4mhtxRJjidqlNb3rxYKDHdECBG3nXNnJc2UytalasaKjK0AkWmsrfTWVxxtibagSKopcKkEdK1a4TtNWLOHBBM1y4OZrdus7amMk14KP9k8xw9l3/EJrBWB1jx2NCsc6M7FBCknSPAdKYHZNhfZaDqnX0oz2ZzdrNwMp+B4I6g0tgVNaaDTE2rOnZvhldRftbo/IH5W6gil69YU8io+z/aZrI0ModGPeU/oehphv4BLqe1w51L+ZfzJ5EVNx2/YrGd8PsT8VlSsDtQS52eZWD2jpYH+wfKnC4hB3Fb4crPe2oSr0UVii2IuoYu2nWPzKCy+sjgetT4fMEO6sKfsOiE7AETt+8J4kxxI615i+yeGxG7oFePeVijjryux68zvWLJFGyGWS7FK1jQdjuKsJgmf3CPnH1qHMewuLs97Dut9Y3ViFed9h+U7R1HNBMPnjWmK3A9t1PeVgQR6g1JrgvGabtOmPOW5fdQ98yPWaNYjEhV3NIP+NQo8fSar4HHYzH3NGHTYe+7bIgPVj+g3PhUtjfSKTn5k7DONu6mMVvlWXtfaEBYCZYToEdC/E+XPlTNlfYSwgBxDNiG2nWSE6TFsHTEgnvauYmmu2EQAKAANgAIA9B0rtntk3nr5UCct7OIhVm7zrOkmdKlhDELxMbajJgkAgEijq2wKibEACZEVr7cU6Rnk5SdstM4UFiYAEk+AG5rkvaPMDeus54mB6DgUw9p+0Gs+zttKD3iOGPgPIfWlt8YnsyhQFjw1b8OParZkyyvhAZhWhFTsKjIq5EhK1rpqdbZJAAknipcTg3T31iuCVrUg6gJj5VpebUxaOaK5bmIto6FAwfr1B/lQ1xvShIIrKl01lccBVWrKWjFe4OzqYCnDAZJrAB2mB86Z8AsTAlSIkmKas27PeycqSDHUcGaXrtnSa6LTA+C8MmdXS28KWgg9IPFT53kZwxALBp8KoPi3YgsxJUAA+AHFXsNjNbD2xLAeNNyLaB60SyvMXtOGtsQfv5EdRVXEqus6Pd6Uf7N5chJuXB3EEt4HwHqTT+OSdXKkHxmGHu2WuYhDaKgkuqkg6QSx0DfYDpSpmWd4a0V7794SNVplIEkCQRtxPpB61lztcpxDh1CWUUkKOSykBAB1JmdPlNLfazOkxOhbakBe8WYDUxOwEAmAO8fjWPLOMflPRxYMl1JfkZsHnVu5ujq3kDBAM7adj40awebEEaogHwHERwPQVxd7BG42I+BBq5hc1vrstxvQnV/umouafaL/AApJ0d2wucJIUtzxPrHT+/nW2dZJhMasXlXWNlcQtxTBEBhyOukyPKuOYHPsSzqmpO8eqx9iKecvyrGP7roI4kahsCAR4RPPnU3HyjmnF0wLj+yTWby2DBDAslyIUosayRvuJAjxI8aasszezhUFi1HdG0mCTyzHxJO/9KiwGLd3NnEDdG74mJYRAmeDM/KieK7JYbE2wQvs2IIV0n/yWYYbevnU+R2063Fb/Glsc3LYj/Wsn60Nx37RLY2TvR4AmefQdfGrGH/ZPZAl8Qx8QqhfqSatW+wuW2iNdxmPgzqPidIBHzpXfotFYV5v7IDYbtn7RgHDqvIkbbgRME/OKv5nmVxl0qYRhvBnV5luo+lHBkeWtoAYjWdKwzEsxBjczvt8ap5l2a/DDUlwNaJghttJPG423O0gDeJB6UxScHbXHv0UyxwZYqONtS9NcMVCahK0azLLWQiRsRKkbgg+B60LNszsK9KMk1aPDyRcXTPBgXMHQYbjziqzoRM9KupinWBqO3APAmqzmSSetEQzBuEcMen36VNmuYtdIkDatcLhw5ILBYBO/XyqsyUKON8FgHuHuCa1FkK5V9iKvZVmjWJ0iZq/2fwKYq+5vGBExMSaHIbVADQvjWU+f4Uwv7x/7qyjTE+JEQezD20ebnwp2/GWiBoNc1AIq1hsUykdQDx400luVHLh2N+Z4xIO80o4m5qanDIsXhbt4NcRVATg+6W8YoL2mt2jiH9gAEgbL7urrFdGLQJTTdAVVqRVqa1aGoBth1qS9bUHumRVUhGyTL8LrdV33IG3Pwp2ztbWFwoRzsTBj8zeBPpQjsZl7PeDwdFuWY+YB0j51fzspfR7Lkw4YiG0nWASI4BiNwdqnlb8eC+lrepM5XmAVnJWYJnfafhvt8agW1FV7l493aYG/H0PPEc1cwl+ORXkzlzaPq9Ptnw1TKz2qqhAGoviHU7jahF59xSxlbBqscIUyyNiD4RFdn7LYwm3acn3lAbnpwd/KuK2zJHqPvXYOzqRaCjeII67R4/rVou0zzdUlwXO1drTiEcbB0A+Ksd/iGHyo32fM2F/6o+ZoZ2t3Sy56NB+I/pRPs8AbHz+5qfsz+EAf2g3HY2EW66qwYkIxWYKwTG55Nc4zK/ZZu6mplMBiSS3mTyfSuhftPYJbw7D3gXUHyKj9YrlBnjqfnWeVuT5PoNHsWmi0lfPr2EcASWC2yxeQyle6EdTIaByRHNdByrN7jM1jHEPbZZkLENqBAJHHjO3FIeEyzFKJTDXyDyRbfjw4qwcNittdu4g6a1ZPqwE1ylKP2KvHhzcNq/DXaOtZdgMPetsiAqBIAJ1BWHDLJOx9dwehpTdzh7jAqCVJB6jbneg2TvesXFc3CArAsssAyg94Eddpjzp87VZaly1+JtssaVJiIYEwrAjk7j1rdpcylweB/6Wjlhkm3d+WJWKOtmcLAJ4HSoEsE8CplBG1WLGIKCABvW+jxrBz2iPWvDYPMVbvEsZNbC5tFdRyYOKVtb7pB3+BirDJJq/lOSvfJCQABuTQ6Osq/ik/dPzrKKf4YueK1lEG6ImYlRq2ot2ayhL7kOYA+FDhZNX8Bce2dSGDVYquyc5NrgzN8vFm6UUyOlVFSr14s7Fm3JrFw9GhbI7GDZ+BWXMKVMEb0dyO04fYTNTZplThyxAg+FdynQjnHryXeyZPsLyKSpjVPT+h2oDldwIz3WcOXIMzJB3lY6Aah8zTJg10YS4OJIHzIG/0rmOaYlVDoWbSpYKoJBLSTJPHJ+lQm9rbPS0mPfjX3Ne0TYUOiYdCGAPtG1FlJMEAT4b8RzG9RWLSaZb4VSbKbyW1vPbZUb3WI28p8PjR/sxkD4nvsSlkbFurEchOm3Vjt6mvJnGUpUkfT6fPDDj3Sdr/JQGW6zpQF2PRQSfkB9alufs9xrwVtBeTDMoPBI2naYA+NddyrAW7K6LSBB18SRt3mO5PrRQNRjDY+zFq9cs62xikvfk+c8yyi/hnCX0KE8HlW2/Kw2PwroPY83EAW4wZCndPXynxp/zPC2ryNbuqro2xB+hHgfOko2ls3BbX3UZQN5MbRufKqQa5RknkbikHu0DhsMrdFYH9BVrspcJw7eIJj50NzVw2GuRxIYf9wNXOxVybLeBY/ala7JegF+1JHY4VBuGLKPNyUG/lH60Q7NZBYwqh3Ae9tLkTpMQQg6DcieTU3a66k4d3iUuXIPh3N/t9aRM6z+67lLJCAcu0x6KBzHjQjBN2aZaiXwljXCXf15Ov2cxQ7ax86uMFcQwDKehAINcFtPixDC/q67qsH6SPoaZ+z/bW7bcJiQAp/OJK/LcqfpTOKMt+UH+2XZ1gvtbC6lUS1v8wUD3lPJiOKXshzHXbNoM2knVpnafTp411PBYtbihgdjXNu2+R/hr4xNkQjGWUcKeseAMzHmfCoSjt/VHg9fR6r40f4fNz6bLeU4NGuqLnubz+kmsziyi3WFr3fmJ670W7P7txJIn5ip8ywNoaiwIYjaPGvXjO6+qPms2Jxm1fVoVDamsXDE8Cr3sqmwr6HDATFUJA98ucCSpqfBYu5ZnQdM8/wBmi65gxYSBE8VDikRn1AbGkTfkZpMHfjLv7xryifs0r2m3C/DiL+By4O4U7Anc0z4js1bCyhJPnWl3KWDSgop+BdUktJ8KpKS4aZnqbdJIVrmVlTxVjD5UzkAL/fjRzDWxy/1q8ceiiFFdKbXSOhBtfqKuEyYJBB3rTHW2cx0rLuYMeKzD3ZPeqacu2UeJdpGr4QG06D8w2/iG6/UVzjAZADfd7o7ltpVTO7c8eA+9dWRNRhRNIPb7ENYR1AIZmgdPe3J+5qcpLtm7TWlsXkHXM4fF3Gwy/wCQsG6fEBpCKehJHPgDThgV9xFAVRsANgABMAelJfZLB+zwwY+9cJc+nC/QT8aacDjAi6mnbj+Q/lUpLbG/JXuW1dIOYrGJZUu7BQNySRsOpJ8KRs17b3HYiwuleA79fMIOh9RS72sz5sRdKqf/AI0MAdGYH3jHIHT4nwgfbvDrt/fNZ9rfLH3JB6zn+MQ69aP6h1/9j9q1/wCMNcuh3GljAgSZIiYPhvzQxMR50QsWkYAkTBkeR6fpS9DbrGp702HX/Tx8JNXuw92EdPMxQYLKOQdyGEeMg1D2UxRRm8/1Ao1dndFn9prn2eHKmJuMD8UJn/xNJGHgkDxP60a7b5mXKI26q8sAY3g7AwYMeR5pYsXyCN9pBjpImJ+Z+dGMf0iyfIwLfIAEmOASI28P74qdbKusEb/fbiOh5oOcTPUx0kzA8Jqe3iYPp/T+lK0ch57BZkyE4dzIXdf4eg8/D4CnbOstGJstbOx5HyII+RNc1S0bWJtNIJgSVnSVdZkdYgg/AV07L8UCpIOwE0K5pj241JOmgfgsqKaYbvCIjj0qzi8u1nU5it/bGZFZcvFua32zzpXJ2wLiMDB23FQ/hqOqnjWHDA024G0GpbTRp097xqBsPRlcKBW34UGu3I7awH+GrKP/AIKsobkNtZ4t0GN9/Ct7uI0mGFLNq+ykMDuDI+FFbmOW4sn3uv8ATyouIu1J0XgyN0qRcuRuBQvDPvRfDXdxFJK10UjE3fLUP5Y9KjXLF6iioqLEXNIqSnLoo4pkNhFTgUNzzJ7WJXTcUEdD1FXNRNeF6Nc2dG49CNj8uFjTbUHQgAX0AgUBz3EsthtJhtLafJogGm/tBmthj7PUNYJGrjccqPGknMF1AjkU2S3HkrAREvajIAAPA8B0FW0vFG3HQgz4HYwT96nGXgd2I8DyNzUOZF2KlxwoQGInT4+JggfKp1wL5ohS9RXBYqANz3p+m386CIhNG8jy5ncFgdA3Y+QpJIaI84FQLOo7whP0pYyS+Q3qB+v86bmVVtPwJRvlB/pSVlr7g+VLHseXRX7T4dlR2BmGB+Z3+9AbYLKGG/6eRpzzi1rR0/eTb6/38K5/h7rIdtjwR0MHqKKlQVHcFlVgfgCPQ7j6EUUy3DF2HQbSSYAHiSeKG/8AENWiEkhYPO3eJj03pgyXMmVhNm3cU+8rBvMQCDt8jSylFF8elySfCD2X2WuXFVF1BeDHjsTPRY2roODwpRAvXqfGpclu2WtK9tAisPdAAgjYgxzxzV8utUikv1GfI3zGqrsHGya9W2av61rNa1XcZ9hVWya3Fs1ZDivFBNDccoEBt15pq2qSa9fDihvDsRU38aypvww8ayu3nbEJNT2KysrURLljmi2D5FZWVOfQ8Q2tVcXyKysrOuypDUL8H0NZWVRCnEX/APsD+Jvu1W8N7z+v61lZTTNM/liVsXUGK9wV7WVJEmVOi/H/AHGmHKunwrKykY0Qjmv+Tc/halnLfy/30NZWUI9hl0F8T7w/g/WucYn/ADH/AI2/3GvKygymPtFzC8U3dmP/AFrKys2To9zTHTOzH+Sf42+y0bFeVlasfyI8TVfzZmV61eVlOZz1avYfisrKBxi+/U13isrK4D7IaysrK44//9k= alt="logo"/>
                <p>Вот она какая, красная планета.</p'''


@app.route('/promotion_image')
def ad():
    return f'''<link rel="stylesheet" type="text/css" href="static/css/style.css" />
    <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
    <title>Колонизация</title>
    <h1>Жди нас, Марс!</h1>
    <img src="static/img/mars.jpeg" alt="logo" />
    <div class="alert alert-dark" role="alert">
                         Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                         Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                         Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                         И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                         Присоединяйся!
                        </div>'''


@app.route('/astronaut_selection')
def select():
    return f''' <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="static/css/style1.css" />
    <title>Отбор астронавтов</title>
                <h1>Анкета претендента</h1>
                <h3>на участие в миссии</h3>
                 <form class="login_form">
                 <div>
                    <input type="text" name="name" placeholder="Введите фамилию" />
                    <p>   </p>
                </div>
                <div>
                    <input type="text" name="name" placeholder="Введите имя" />
                    <p>   </p>
                </div>
                <div>
                    <input type="text" name="name" placeholder="Введите адрес почты" />
                    <p>   </p>
                </div>
                <div>
                    <label>Какое у вас образование?</label>
                    <input type="text" name="name" placeholder="Начальное" />
                    <p>   </p>
                </div>
                <div>
                    <ladel>Какие у Вас есть профессии?</ladel>
                    <p> </p>
                    <ladel>Инженер-исследователь</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Инженер-строитель</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Пилот</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Meтeopoлог</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Инженер по жизнеобеспечению</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Инженер по радиационной защите</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Bpaч</ladel>
                    <input type="checkbox" name="rules" />
                    <p>   </p>
                    <ladel>Эзобиолог</ladel>
                    <input type="checkbox" name="rules" />
                </div>
                <div>
                    <label> Укажите пол</label>
                    <p>  </p>
                    <input type="radio" name="sex" value="0" />Мужcкой 
                    <p> </p>
                    <input type="radio" name="sex" value="0" />Женский
                </div>
                <div>
                    <label>Почему Вы хотите принять участие в миссии?</label>
                    <p> </p>
                    <textarea placeholder="Введите текст сообщения....."></textarea>
                </div
                <div> 
                    <ladel>Загрузите фото:</ladel>
                    <p> </p>
                    <input type="file" name="rs" />
                    <p>   </p>
                    <ladel>Готовы остаться на Марсе?</ladel>
                    <input type="checkbox" name="rules" />
                    <p> </p>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </div>
             </form>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<title>Варианты выбора</title>
    <h1>Моё предложение: {planet_name}</h1>
    



'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')