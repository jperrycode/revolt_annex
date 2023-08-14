# class AppBasedRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'schedule':
#             return 'default'
#         elif model._meta.app_label == 'archive':
#             return 'image_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'schedule':
#             return 'default'
#         elif model._meta.app_label == 'archive':
#             return 'image_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'schedule':
#             return db == 'default'
#         elif app_label == 'archive':
#             return db == 'image_db'
#         return None
