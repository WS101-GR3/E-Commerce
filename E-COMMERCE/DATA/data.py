import openpyxl
from PRODUCT.models import Parts, PackageBundle
from STORE.models import Store

def import_excel_data(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active

    # Iterates the spreadsheet column and simultaneously insert into Parts model
    for row in worksheet.iter_rows(min_row=2):  # Assuming header row is the first row
        name = row[0].value
        category = row[1].value
        description = row[2].value
        price_str = row[3].value
        price = float(str(price_str).replace(',', '').replace('\u200b', ''))
        # Create a new model instance
        try:
            model_instance = Parts(
                parts_store=Store.objects.get(store_id=4),
                parts_category=category,
                parts_name=name,
                parts_description=description,
                parts_price=price,
                parts_quantity=8
            )
        except :
            return 'Something is amiss'

        # Save the instance to the database
        model_instance.save()

import random
def generatePackage(packageModel, partsModel, numberofInstances, InstancesName):

    # randomly selects an instance within a certain category
    Motherboards = partsModel.objects.filter(parts_category='Motherboard')
    CPUs = partsModel.objects.filter(parts_category='CPU')
    Storages = partsModel.objects.filter(parts_category='Storage')
    Memories = partsModel.objects.filter(parts_category='Memory')
    PowerSupplies = partsModel.objects.filter(parts_category='Power Supply Unit')
    CPU_Coolers = partsModel.objects.filter(parts_category='CPU Cooler')
    Graphic_Cards = partsModel.objects.filter(parts_category='Graphics Card')
    Cases = partsModel.objects.filter(parts_category='Case')


    # Will populate the PackageBundle Model with the randomly selected instance above
    for bundle in range(1,numberofInstances+1):
        # Get random instance per parts
        motherboard = random.choice(Motherboards)
        cpu = random.choice(CPUs)
        storage = random.choice(Storages)
        memory = random.choice(Memories)
        powersupply = random.choice(PowerSupplies)
        cpu_cooler = random.choice(CPU_Coolers)
        gpu = random.choice(Graphic_Cards)
        case = random.choice(Cases)

        # totals all parts that are randomly selected
        total_price = motherboard.parts_price + cpu.parts_price + storage.parts_price + memory.parts_price + powersupply.parts_price + cpu_cooler.parts_price + gpu.parts_price + case.parts_price


        try:
            package_instance = packageModel(
                bundle_category = 'UserBuild',
                bundle_name = f'{InstancesName} {bundle}',
                motherboard_unit = motherboard,
                processor_unit = cpu,
                storage_unit = storage,
                memory_unit = memory,
                PSU_unit = powersupply,
                CPU_cooler_unit = cpu_cooler,
                GPU_unit = gpu,
                case_unit = case,

                bundle_total_price = total_price 
            )
        except:
            return 'ERROR'
        
        # saves data
        package_instance.save()