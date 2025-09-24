from flask import Flask, jsonify, Blueprint
from .Errors import general_error_handler
class EnrichedApp(Blueprint):

    def __init__(self, name=__name__, prefix='/api'):
        super().__init__(name=name, url_prefix=f'{prefix}')

        self.add_url_rule(f'{prefix}/test', view_func=self.api_test, methods=['POST', 'GET']) 
        self.register_error_handler(Exception, general_error_handler)


    def register_blueprints(self, bpclasses):
        for bpc in bpclasses:
            bp = bpc()
            self.register_blueprint(bp)

    def api_test(v):
        print('test')
        return jsonify({'works':True})
    
        
