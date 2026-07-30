extends SceneTree
func _initialize() -> void:
    var args := OS.get_cmdline_user_args()
    var asset := ""
    for i in range(args.size()):
        if args[i] == "--asset" and i + 1 < args.size(): asset = args[i + 1]
    if asset.is_empty():
        push_error("missing --asset")
        quit(2); return
    var resource := load(asset)
    if resource == null or not resource is PackedScene:
        push_error("asset did not import as PackedScene")
        quit(3); return
    var instance := (resource as PackedScene).instantiate()
    if instance == null:
        push_error("could not instantiate")
        quit(4); return
    var nodes := 0
    var stack: Array[Node] = [instance]
    while not stack.is_empty():
        var node := stack.pop_back(); nodes += 1
        for child in node.get_children(): stack.append(child)
    print("PRODUCTION_TOOLKIT_GODOT_IMPORT: PASS nodes=", nodes)
    instance.queue_free(); quit(0)
