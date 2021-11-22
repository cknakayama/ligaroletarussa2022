import cartolafc

api = cartolafc.Api()
try:
    api.liga(slug='')
except cartolafc.CartolaFCError:
    print('erro')
else:
    print('ok')