# vim: set encoding=utf-8

#
#  Copyright (c) 2015 Intel Corporation 
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import unittest
import trustedanalytics as ta
import connect

# show full stack traces
ta.errors.show_details = True
ta.server.uri = "atk-34157d69-65f4-426f-ac14.demo-gotapaas.com"
ta.loggers.set_api()
# TODO: port setup should move to a super class
if ta.server.port != 19099:
    ta.server.port = 19099
#ta.connect('/root/demo.creds')
connect.connect()

class ModelLinearRegressionTest(unittest.TestCase):
    def testLinearRegression(self):
        print "define csv file"
        csv = ta.CsvFile("hdfs://nameservice1/org/intel/hdfsbroker/userspace/b61d4808-e761-45c3-bd54-afcb05b84a8b/49959598-e926-400c-8095-be3a0eaa74e3/000000_1",

        schema = [
##                  ("y",ta.float64),
##                  ("1",ta.float64),
##                  ("2",ta.float64),
##                  ("3",ta.float64),
##                  ("4",ta.float64),
##                  ("5",ta.float64),
##                  ("6",ta.float64),
##                  ("7",ta.float64),
##                  ("8",ta.float64),
##                  ("9",ta.float64),
##                  ("10",ta.float64)])

                  ("GXY",ta.int32),
                  ("Age",ta.int32),
                  ("Sex",ta.int32),
                  ("Height",ta.float64),
                  ("Weight",ta.float64),
                  ("BMI",ta.float64),
                  ], skip_header_lines=1)


        print "create frame"
        frame = ta.Frame(csv,'LinearRegressionSampleFrame_22')

        print "Initializing a LinearRegressionModel object"
        model = ta.LinearRegressionModel(name='myLinearRegressionModel_22')

        print "Training the model on the Frame"
        model.train(frame,'GXY',['Age','Sex','Height','Weight','BMI'])

##                    'y',['1','2','3','4','5','6','7','8','9','10'])


        output = model.predict(frame)
        print output.column_names
#        self.assertEqual(output.column_names,['GXY',,'QJD','DCJC','MJJC','RUT','PGI/PGII','Ca2','P3','K','Na','CI','predicted_value'])
         #['y','1','2','3','4','5','6','7','8','9','10','predicted_value'])



if __name__ == "__main__":
    unittest.main()
