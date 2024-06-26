import flet as ft
from cryptoApi import get_coin_names, get_crypto_info

def main(page: ft.Page):
    def on_change(event):
        update_crypto_info()

    def update_crypto_info():
        if combo_box.value is None:
            return
        
        info = get_crypto_info(combo_box.value)
        
        if rb.value == "basit":
            selected_item.content = ft.Column(
                [
                    ft.Text(f"{combo_box.value}", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Fiyat: {info['lastPrice']}", size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        elif rb.value == "detayli":
            selected_item.content = ft.Column(
                [
                    ft.Text(f"{combo_box.value}", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Fiyat: {info['lastPrice']}", size=16),
                    ft.Text(f"24s Değişim: {info['priceChangePercent']}%", size=16),
                    ft.Text(f"En Yüksek Fiyat: {info['highPrice']}", size=16),
                    ft.Text(f"En Düşük Fiyat: {info['lowPrice']}", size=16),
                    ft.Text(f"Hacim: {info['volume']}", size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        
        selected_item.update()
        page.update()

    def coins_update():
        coin_list = ["BTCUSDT", "ETHUSDT", "BNBUSDT","LUNAUSDT","USDTTRY"]
        prices = {coin: get_crypto_info(coin)['lastPrice'] for coin in coin_list}
        
        some_coins.content = ft.Column(
            [
                ft.Text("SIK GEZİLENLER", size=18, weight=ft.FontWeight.BOLD,font_family='Calibri',color=ft.colors.BLUE),
                ft.Text(f"BTC: {prices['BTCUSDT']} USDT", size=16,color=ft.colors.BLUE),
                ft.Text(f"ETH: {prices['ETHUSDT']} USDT", size=16,color=ft.colors.BLUE),
                ft.Text(f"BNB: {prices['BNBUSDT']} USDT ", size=16,color=ft.colors.BLUE),
                ft.Text(f"LUNA: {prices['LUNAUSDT']} USDT", size=16,color=ft.colors.BLUE),
                ft.Text(f"USDT: {prices['USDTTRY']} TRY", size=16,color=ft.colors.BLUE),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )
        some_coins.update()
        page.update()
    
    
    
    
    
    combo_box = ft.Dropdown(
        hint_text="Kripto para birimi seçin",
        value=None,
        label="Kripto Para",
        item_height=48,
        width=300,
        autofocus=True,
        options=[
            ft.dropdown.Option(text=name) for name in get_coin_names()
        ],
        on_change=on_change,
    )
    
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.CURRENCY_BITCOIN),
        bgcolor=ft.colors.BLUE,
        middle=ft.Text("Kripto Para Aracı", font_family="Calibri", size=20),
    )

    selected_item = ft.Container(
        content=None,
        padding=20,
        border_radius=8,
        bgcolor=ft.colors.BACKGROUND,
        width=350,
        height=250,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=3,
            color=ft.colors.BLACK12,
            offset=ft.Offset(2, 2)
        ),
        alignment=ft.alignment.center,
    )

    rb = ft.RadioGroup(
        value='basit', 
        on_change=on_change,  
        content=ft.Column([
            ft.CupertinoRadio(value='basit', label='Basit', active_color=ft.colors.BLUE,),
            ft.CupertinoRadio(value='detayli', label='Detaylı', active_color=ft.colors.BLUE),
        ]),
    )

    some_coins = ft.Container(
        content=None,
        padding=20,
        border_radius=8,
        bgcolor=ft.colors.BACKGROUND,
        width=350,
        height=250,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=3,
            color=ft.colors.BLACK12,
            offset=ft.Offset(2, 2)
        ),
        alignment=ft.alignment.center,
    )

    
    
    main = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    combo_box,
                    rb,
                    selected_item,
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            some_coins,
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
    )

    page.add(
        ft.Container(
            content=main,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.BLACK12,
        )
    )

    def update_periodically():
        while True:
            update_crypto_info()
            coins_update()

    import threading
    threading.Thread(target=update_periodically, daemon=True).start()

ft.app(target=main)
