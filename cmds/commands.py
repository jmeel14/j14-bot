class Command:
	global defined

	defined = []

	def __init__(self, name):
		self.name = name
		self.process = None
		self.bot = None

		defined.append(self)