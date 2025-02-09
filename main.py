import flet as ft
import loader

g_url = ''

def mn(page: ft.Page):
   def file_picker(path):
      path = path.path
      if path:
         end_text.value = 'Началось скачивание...'
         end_text.color = ft.Colors.RED
         page.update()
         end_text.value = loader.download_video(g_url, path)
         end_text.color = ft.Colors.GREEN
         page.update()

   def start_download(x):
      pick_path.get_directory_path('Выберите куда скачать видео')
   def on_change_url(x):
      global g_url
      end_text.value = ''
      if download_button in video_row.controls:
         video_row.controls.remove(download_button)
      url = url_field.value
      url_field.disabled = True
      page.update()
      if url:
         video_name.value = 'Поиск...'
         page.update()
         name = loader.video_name(url)
         video_name.value = f'{name}'
         if name != 'Не найдено':
            g_url = url
            video_row.controls.append(download_button)
      else:
         video_name.value = 'Видео не выбрано'
      url_field.disabled = False
      page.update()
   c = ft.MainAxisAlignment.CENTER
   page.title = 'Скачиватель видео с ютуба'
   page.theme_mode = 'light'
   page.vertical_alignment = ft.MainAxisAlignment.START
   page.window.height = 300
   page.window.width = 600
   page.window.resizable = True
   guide = ft.Text(value='Чтобы скачать видео, вставь URL адрес в поле ниже:', text_align=ft.TextAlign.CENTER)
   url_field = ft.TextField(width=450, label='URL', on_submit=on_change_url)
   video_name = ft.Text(value='Видео не выбрано')
   download_button = ft.IconButton(icon=ft.Icons.DOWNLOAD, on_click=start_download)
   video_row = ft.Row([video_name], alignment=c)
   pick_path = ft.FilePicker(on_result=file_picker)
   end_text = ft.Text(value='', color=ft.Colors.GREEN)
   page.add(ft.Row([guide], alignment=c), ft.Row([url_field], alignment=c), video_row, ft.Row([end_text], alignment=c), pick_path)
   page.update()

ft.app(target=mn)