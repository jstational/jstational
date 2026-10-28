public class Registry {
    private RegKey main;

    public Registry() {
        main = new RegKey("");
    }

    public ObjectMap<String, RegKey> getSubkeys() {
        return main.getSubkeys();
    }

    public RegKey getKey(String name) {
        return main.getSubkey(name);
    }

    public RegKey addKey(String name) {
        main.addSubkey(name);
    }

    public RegKey addKey(RegKey key) {
        main.addSubkey(key);
    }

    public static class RegKey {
        private String name;
        private ObjectMap<String, RegKey> subkeys;

        public RegKey(String name) {
            this.name = name;
            subkeys = new ObjectMap<>();
        }

        public ObjectMap<String, RegKey> getSubkeys() {
            return subkeys.copy();
        }

        public String getName() {
            return name;
        }

        public RegKey getSubkey(String name) {
            RegKey cur = subkeys.get(name);
            if(cur != null) return cur;

            RegKey newKey = new RegKey(name);
            return addSubkey(newKey);
        }

        public RegKey addSubkey(String name) {
            return subkeys.put(name, new RegKey(name));
        }

        public RegKey addSubkey(RegKey key) {
            return subkeys.put(key.getName(), key);
        }
    }
}