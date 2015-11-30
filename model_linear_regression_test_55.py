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
import os

# show full stack traces
ta.errors.show_details = True
ta.server.uri = "atk-ed1f8bd2-45e7-4396-8267.10.239.70.85.xip.io"
ta.loggers.set_api()
# TODO: port setup should move to a super class
if ta.server.port != 19099:
    ta.server.port = 19099
connect.connect()

class ModelLinearRegressionTest(unittest.TestCase):
    def testLinearRegression(self):
        print "define csv file"
	os.environ['http_proxy'] = 'http://child-prc.intel.com:913'
        os.environ['https_proxy'] = 'http://child-prc.intel.com:913'
	atkPocLinar55="hdfs://nameservice1/org/intel/hdfsbroker/userspace/8ccd576b-c779-44ff-8189-66cd2882b5d1/524b31df-eaa5-42a3-9a52-b5daeab69ad4/000000_1"
        csv = ta.CsvFile(atkPocLinar55,

        schema = [
                  ("GXY",ta.float32),
                  ("Age",ta.float32),
                  ("Sex",ta.float32),
                  ("Height",ta.float64),
                  ("Weight",ta.float64),
                  ("BMI",ta.float64)
                  ], skip_header_lines=1)
    
        frame_name="LinearRegressionFrame"
        if frame_name in ta.get_frame_names():
             ta.drop_frames(frame_name)

        print "create frame"
        frame = ta.Frame(csv,frame_name)

        model_name="myLinearModel"
        if model_name in ta.get_model_names():
            ta.drop_models(model_name)

        print "Initializing a LinearRegressionModel object"
        model = ta.LinearRegressionModel(name=model_name)

        print "Training the model on the Frame"
        model.train(frame,
                    'GXY',['Age','Sex','Height','Weight','BMI'])




        output = model.predict(frame)
        print output.column_names

if __name__ == "__main__":
    unittest.main()
