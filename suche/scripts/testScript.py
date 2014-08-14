from linguistic.NLProcess import *
from plugin.pluginProcess import *
def run():
    a=NLGrammar('temperature for Kathmandu')
    result=a.compareGetId()
    q=PluginProcessor(result[0],result[1])
    output=q.dispatchandRead()
    print(output)
    