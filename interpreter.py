class program:
	memory = [];
	integer = 1;
	instructions = [];
	factors = [];
	memPointer = 0;
	inPointer = 0;

	class primeIterator:
		def __init__(self):
			self.primes = [2];

		def __iter__(self):
			return(self);

		def __next__(self):
			test = self.primes[-1]+2;
			while(1):
				divisible = False;
				index = 1;
				while(primes[index] <= test**0.5):
					if(test % primes[index] == 0):
						divisible = True;
					index += 1;
				if(divisible):
					return(test);
				test += 2;

	def __init__(self, integer):
		self.integer = integer;
		self.memPointer = 0;
		self.inPointer = 0;
		for i in range(0, 1000):
			self.memory.append(0);

	def factoriser(self):
		primes = primeIterator();
		while(self.integer != 1):
			divisible = False;
			prime = iter(primes);
			while(self.integer % prime == 0):
				self.integer = self.integer/prime;
				divisible = True;
			self.factors.append(divisible);

	def createInstructions(self):
		if(len(self.factors) % 2 == 1):
			self.factors.append(0);
		for i in range(0, len(self.factors), 2):
			if(self.factors[i] == 0 and self.factors[i+1] == 0):
				self.instructions.append('r');
			elif(self.factors[i] == 0 and self.factors[i+1] == 1):
				self.instructions.append('+');
			elif(self.factors[i] == 1 and self.factors[i+1] == 0):
				self.instructions.append('j');
			elif(self.factors[i] == 1 and self.factors[i+1] == 1):
				self.instructions.append('e');

	def runProgram(self):
		while(self.instructions[self.inPointer] != 'e'):
			if(self.instructions[self.inPointer] == 'r'):
				self.memPointer = (self.memPointer + 1) % 1000;
			elif(self.instructions[self.inPointer] == '+'):
				self.memory[self.memPointer] = (self.memory[self.memPointer] + 1) % 256;
			elif(self.instructions[self.inPointer] and self.memory[self.memPointer] == 0):
				self.inPointer = (self.inPointer + 2520) % len(self.inPointer);
			self.inPointer = (self.inPointer + 1) % len(self.inPointer);
		return(self.memory);

	def loadProgram(self, instructions):
		self.instructions = instructions;