# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('API_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('EAN', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('stock', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('API', ['Product'])

        # Adding model 'GroceryList'
        db.create_table('API_grocerylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('API', ['GroceryList'])

        # Adding model 'GroceryList_Product'
        db.create_table('API_grocerylist_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['API.Product'])),
            ('grocerylist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['API.GroceryList'])),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('API', ['GroceryList_Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('API_product')

        # Deleting model 'GroceryList'
        db.delete_table('API_grocerylist')

        # Deleting model 'GroceryList_Product'
        db.delete_table('API_grocerylist_product')


    models = {
        'API.grocerylist': {
            'Meta': {'object_name': 'GroceryList'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['API.Product']", 'through': "orm['API.GroceryList_Product']", 'symmetrical': 'False'}),
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