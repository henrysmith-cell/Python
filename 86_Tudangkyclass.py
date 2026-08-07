class PluginRegistryMeta(type):
    """Metaclass tự động ghi nhận mọi Class Plugin được định nghĩa"""

    _registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # Bỏ qua không đăng ký Base Class gốc
        if name != "BasePlugin":
            plugin_name = namespace.get("plugin_name", name.lower())
            mcs._registry[plugin_name] = cls
            print(
                f"⚙️  [Metaclass] Đã tự động đăng ký Plugin: '{plugin_name}' -> {name}"
            )
        return cls

    @classmethod
    def lay_plugin(mcs, name: str):
        return mcs._registry.get(name)

    @classmethod
    def danh_sach_plugins(mcs):
        return dict(mcs._registry)


# Base Class sử dụng Metaclass
class BasePlugin(metaclass=PluginRegistryMeta):
    def thuc_thi(self):
        raise NotImplementedError


# Khai báo các Plugin con - Metaclass sẽ tự động bắt lấy và đăng ký
class ExportPDFPlugin(BasePlugin):
    plugin_name = "pdf_exporter"

    def thuc_thi(self):
        return "📄 Xuất dữ liệu ra file PDF thành công!"


class ExportExcelPlugin(BasePlugin):
    plugin_name = "excel_exporter"

    def thuc_thi(self):
        return "📊 Xuất dữ liệu ra file Excel thành công!"


def main():
    print("\n--- DEMO METACLASS CLASS REGISTRY PATTERN ---")

    print("\nDanh sách các Plugin hiện có trong hệ thống:")
    for name, cls in PluginRegistryMeta.danh_sach_plugins().items():
        print(f" - {name}: {cls.__name__}")

    print("\nChạy thử Plugin theo tên được gọi động:")
    ten_plugin_can_goi = "pdf_exporter"
    plugin_cls = PluginRegistryMeta.lay_plugin(ten_plugin_can_goi)

    if plugin_cls:
        instance = plugin_cls()
        print(instance.thuc_thi())


if __name__ == "__main__":
    main()
