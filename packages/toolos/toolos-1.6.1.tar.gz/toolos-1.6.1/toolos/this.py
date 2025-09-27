import toolos as engine

class YourApp(engine.Api):
    
    def __init__(self, settings_path="settings.json", standard_language_library=True):
        super().__init__(settings_path, standard_language_library)
        
        yourneed = self.Settings.Global("yourneed", "default_value")
        # Returning "default_value" if "yourneed" is not set in settings.json
        # else returns the value of your key "yourneed"
        
        # Practical Example:
        if mods_enabled := self.Settings.Global("mods_enabled", False):
            self.StateMachine.SetKeyState("mods", mods_enabled)
        else:
            self.StateMachine.SetKeyState("mods", mods_enabled)
            
        # Check if settings were updated and reload if necessary
        if self.Settings.CheckIfUpdate():
            self.Settings.Update()
            
