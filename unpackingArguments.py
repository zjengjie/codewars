def spread(func, args):
	return func(*args)

#other solutions
spread=apply

ef spread(func, args):
	return eval('func'+ '('+','.join(str(a) for a in args)+')')
