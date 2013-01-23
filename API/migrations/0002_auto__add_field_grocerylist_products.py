# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GroceryList.products'
        db.add_column('API_grocerylist', 'products',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GroceryList.products'
        db.delete_column('API_grocerylist', 'products')


    models = {
        'API.grocerylist': {
            'Meta': {'object_name': 'GroceryList'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'API.grocerylist_product': {
            'Meta': {'object_name': 'GroceryList_Product'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'grocerylist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['API.GroceryList']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['API.Product']"})
        },
        'API.product': {
            'EAN': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'stock': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['API']