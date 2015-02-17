
                
Getting Started
***************
                
                
import the energiscore library. 

                
.. code:: python

    import energiscore as es # Imports the Energiscore Library
                
Client Instantiation and Authentication
***************************************
                
                
``EnergiStreamClient`` takes a valid username and password and establishes a unique session with temporary credentials.

                
.. code:: python

    stream = es.EnergiStreamClient('***REMOVED***', '***REMOVED***', include_sensors=True) 
                
``authenticate`` uses the user credentials to authenticate the instantiated client in the event that authentication was not previously established or has lapsed.

                
.. code:: python

    stream.authenticate



.. parsed-literal::

    <bound method EnergiStreamClient.authenticate of <energiscore.io.stream.EnergiStreamClient object at 0x10609b4d0>>



                
``is_authenticated`` returns a simple boolean true or false when asked if the client authentication is still valid.

                
.. code:: python

    stream.is_authenticated



.. parsed-literal::

    True



                
External Data
*************
                
                
``get_weather`` returns a dataframe of hourly temperature and relative humidity data for the instantiated client's associated physical location. Note : This data is collected from third party sources. Weather ID is an energistream unique key and not associated to any third party ID schema.

                
.. code:: python

    stream.get_weather(weather_id = 102, start = '12/29/2014', end = '1/29/2015')



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>c</th>
          <th>f</th>
          <th>h</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-12-29 00:00:00+00:00</th>
          <td> 15.6</td>
          <td> 60</td>
          <td> 42</td>
        </tr>
        <tr>
          <th>2014-12-29 01:00:00+00:00</th>
          <td> 15.0</td>
          <td> 59</td>
          <td> 48</td>
        </tr>
        <tr>
          <th>2014-12-29 02:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 55</td>
        </tr>
        <tr>
          <th>2014-12-29 03:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 53</td>
        </tr>
        <tr>
          <th>2014-12-29 04:00:00+00:00</th>
          <td> 12.2</td>
          <td> 54</td>
          <td> 57</td>
        </tr>
        <tr>
          <th>2014-12-29 05:00:00+00:00</th>
          <td> 12.2</td>
          <td> 54</td>
          <td> 53</td>
        </tr>
        <tr>
          <th>2014-12-29 06:00:00+00:00</th>
          <td> 11.1</td>
          <td> 52</td>
          <td> 55</td>
        </tr>
        <tr>
          <th>2014-12-29 07:00:00+00:00</th>
          <td> 10.0</td>
          <td> 50</td>
          <td> 59</td>
        </tr>
        <tr>
          <th>2014-12-29 08:00:00+00:00</th>
          <td> 10.0</td>
          <td> 50</td>
          <td> 59</td>
        </tr>
        <tr>
          <th>2014-12-29 09:00:00+00:00</th>
          <td>  9.4</td>
          <td> 49</td>
          <td> 61</td>
        </tr>
        <tr>
          <th>2014-12-29 10:00:00+00:00</th>
          <td>  8.9</td>
          <td> 48</td>
          <td> 63</td>
        </tr>
        <tr>
          <th>2014-12-29 11:00:00+00:00</th>
          <td>  8.3</td>
          <td> 47</td>
          <td> 63</td>
        </tr>
        <tr>
          <th>2014-12-29 12:00:00+00:00</th>
          <td>  7.8</td>
          <td> 46</td>
          <td> 66</td>
        </tr>
        <tr>
          <th>2014-12-29 13:00:00+00:00</th>
          <td>  8.3</td>
          <td> 47</td>
          <td> 63</td>
        </tr>
        <tr>
          <th>2014-12-29 14:00:00+00:00</th>
          <td>  9.4</td>
          <td> 49</td>
          <td> 59</td>
        </tr>
        <tr>
          <th>2014-12-29 15:00:00+00:00</th>
          <td> 11.7</td>
          <td> 53</td>
          <td> 55</td>
        </tr>
        <tr>
          <th>2014-12-29 16:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 55</td>
        </tr>
        <tr>
          <th>2014-12-29 17:00:00+00:00</th>
          <td> 15.6</td>
          <td> 60</td>
          <td> 52</td>
        </tr>
        <tr>
          <th>2014-12-29 18:00:00+00:00</th>
          <td> 16.1</td>
          <td> 61</td>
          <td> 52</td>
        </tr>
        <tr>
          <th>2014-12-29 19:00:00+00:00</th>
          <td> 16.1</td>
          <td> 61</td>
          <td> 52</td>
        </tr>
        <tr>
          <th>2014-12-29 20:00:00+00:00</th>
          <td> 17.2</td>
          <td> 63</td>
          <td> 48</td>
        </tr>
        <tr>
          <th>2014-12-29 21:00:00+00:00</th>
          <td> 17.2</td>
          <td> 63</td>
          <td> 50</td>
        </tr>
        <tr>
          <th>2014-12-29 22:00:00+00:00</th>
          <td> 17.8</td>
          <td> 64</td>
          <td> 48</td>
        </tr>
        <tr>
          <th>2014-12-29 23:00:00+00:00</th>
          <td> 16.7</td>
          <td> 62</td>
          <td> 54</td>
        </tr>
        <tr>
          <th>2014-12-30 00:00:00+00:00</th>
          <td> 15.6</td>
          <td> 60</td>
          <td> 58</td>
        </tr>
        <tr>
          <th>2014-12-30 01:00:00+00:00</th>
          <td> 15.0</td>
          <td> 59</td>
          <td> 62</td>
        </tr>
        <tr>
          <th>2014-12-30 02:00:00+00:00</th>
          <td> 13.9</td>
          <td> 57</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>2014-12-30 03:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>2014-12-30 04:00:00+00:00</th>
          <td> 12.8</td>
          <td> 55</td>
          <td> 69</td>
        </tr>
        <tr>
          <th>2014-12-30 05:00:00+00:00</th>
          <td> 12.8</td>
          <td> 55</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2015-01-27 18:00:00+00:00</th>
          <td> 21.1</td>
          <td> 70</td>
          <td> 47</td>
        </tr>
        <tr>
          <th>2015-01-27 19:00:00+00:00</th>
          <td> 22.2</td>
          <td> 72</td>
          <td> 43</td>
        </tr>
        <tr>
          <th>2015-01-27 20:00:00+00:00</th>
          <td> 23.3</td>
          <td> 74</td>
          <td> 37</td>
        </tr>
        <tr>
          <th>2015-01-27 21:00:00+00:00</th>
          <td> 22.2</td>
          <td> 72</td>
          <td> 44</td>
        </tr>
        <tr>
          <th>2015-01-27 22:00:00+00:00</th>
          <td> 22.2</td>
          <td> 72</td>
          <td> 46</td>
        </tr>
        <tr>
          <th>2015-01-27 23:00:00+00:00</th>
          <td> 21.7</td>
          <td> 71</td>
          <td> 49</td>
        </tr>
        <tr>
          <th>2015-01-28 00:00:00+00:00</th>
          <td> 20.6</td>
          <td> 69</td>
          <td> 49</td>
        </tr>
        <tr>
          <th>2015-01-28 01:00:00+00:00</th>
          <td> 19.4</td>
          <td> 67</td>
          <td> 57</td>
        </tr>
        <tr>
          <th>2015-01-28 02:00:00+00:00</th>
          <td> 18.9</td>
          <td> 66</td>
          <td> 63</td>
        </tr>
        <tr>
          <th>2015-01-28 03:00:00+00:00</th>
          <td> 18.3</td>
          <td> 65</td>
          <td> 63</td>
        </tr>
        <tr>
          <th>2015-01-28 04:00:00+00:00</th>
          <td> 17.8</td>
          <td> 64</td>
          <td> 60</td>
        </tr>
        <tr>
          <th>2015-01-28 05:00:00+00:00</th>
          <td> 16.7</td>
          <td> 62</td>
          <td> 65</td>
        </tr>
        <tr>
          <th>2015-01-28 06:00:00+00:00</th>
          <td> 16.1</td>
          <td> 61</td>
          <td> 70</td>
        </tr>
        <tr>
          <th>2015-01-28 07:00:00+00:00</th>
          <td> 15.6</td>
          <td> 60</td>
          <td> 70</td>
        </tr>
        <tr>
          <th>2015-01-28 08:00:00+00:00</th>
          <td> 14.4</td>
          <td> 58</td>
          <td> 75</td>
        </tr>
        <tr>
          <th>2015-01-28 09:00:00+00:00</th>
          <td> 14.4</td>
          <td> 58</td>
          <td> 75</td>
        </tr>
        <tr>
          <th>2015-01-28 10:00:00+00:00</th>
          <td> 13.9</td>
          <td> 57</td>
          <td> 74</td>
        </tr>
        <tr>
          <th>2015-01-28 11:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 75</td>
        </tr>
        <tr>
          <th>2015-01-28 12:00:00+00:00</th>
          <td> 12.8</td>
          <td> 55</td>
          <td> 77</td>
        </tr>
        <tr>
          <th>2015-01-28 13:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 75</td>
        </tr>
        <tr>
          <th>2015-01-28 14:00:00+00:00</th>
          <td> 13.3</td>
          <td> 56</td>
          <td> 72</td>
        </tr>
        <tr>
          <th>2015-01-28 15:00:00+00:00</th>
          <td> 14.4</td>
          <td> 58</td>
          <td> 72</td>
        </tr>
        <tr>
          <th>2015-01-28 16:00:00+00:00</th>
          <td> 16.7</td>
          <td> 62</td>
          <td> 62</td>
        </tr>
        <tr>
          <th>2015-01-28 17:00:00+00:00</th>
          <td> 19.4</td>
          <td> 67</td>
          <td> 51</td>
        </tr>
        <tr>
          <th>2015-01-28 18:00:00+00:00</th>
          <td> 21.7</td>
          <td> 71</td>
          <td> 44</td>
        </tr>
        <tr>
          <th>2015-01-28 19:00:00+00:00</th>
          <td> 23.3</td>
          <td> 74</td>
          <td> 37</td>
        </tr>
        <tr>
          <th>2015-01-28 20:00:00+00:00</th>
          <td> 23.9</td>
          <td> 75</td>
          <td> 36</td>
        </tr>
        <tr>
          <th>2015-01-28 21:00:00+00:00</th>
          <td> 23.3</td>
          <td> 74</td>
          <td> 41</td>
        </tr>
        <tr>
          <th>2015-01-28 22:00:00+00:00</th>
          <td> 22.2</td>
          <td> 72</td>
          <td> 46</td>
        </tr>
        <tr>
          <th>2015-01-28 23:00:00+00:00</th>
          <td> 22.2</td>
          <td> 72</td>
          <td> 44</td>
        </tr>
      </tbody>
    </table>
    <p>744 rows × 3 columns</p>
    </div>



                
Energistream Data and Metadata
******************************
                
                
``get_energy`` accepts a sensor ID and returns a dataframe relating active and reactive energy, current and voltage RMS, and total Energy.

                
.. code:: python

    stream.get_energy(3505, start = '12/29/2014', end = '1/29/2015', tz = 'local')



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>activeEnergy</th>
          <th>currentRMS</th>
          <th>powerFactor</th>
          <th>reactiveEnergy</th>
          <th>sensorId</th>
          <th>totalEnergy</th>
          <th>voltageRMS</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-12-29 00:01:00-08:00</th>
          <td> 43566.626</td>
          <td> 27.44</td>
          <td> 0.93</td>
          <td> 13801.665</td>
          <td> 3505</td>
          <td> 45700.513</td>
          <td> 490.52</td>
        </tr>
        <tr>
          <th>2014-12-29 00:02:00-08:00</th>
          <td> 43566.850</td>
          <td> 27.74</td>
          <td> 0.94</td>
          <td> 13801.740</td>
          <td> 3505</td>
          <td> 45700.749</td>
          <td> 490.00</td>
        </tr>
        <tr>
          <th>2014-12-29 00:03:00-08:00</th>
          <td> 43567.077</td>
          <td> 30.02</td>
          <td> 0.93</td>
          <td> 13801.816</td>
          <td> 3505</td>
          <td> 45700.989</td>
          <td> 489.29</td>
        </tr>
        <tr>
          <th>2014-12-29 00:04:00-08:00</th>
          <td> 43567.310</td>
          <td> 28.41</td>
          <td> 0.93</td>
          <td> 13801.901</td>
          <td> 3505</td>
          <td> 45701.236</td>
          <td> 491.54</td>
        </tr>
        <tr>
          <th>2014-12-29 00:05:00-08:00</th>
          <td> 43567.541</td>
          <td> 27.81</td>
          <td> 0.94</td>
          <td> 13801.986</td>
          <td> 3505</td>
          <td> 45701.482</td>
          <td> 491.18</td>
        </tr>
        <tr>
          <th>2014-12-29 00:06:00-08:00</th>
          <td> 43567.770</td>
          <td> 28.68</td>
          <td> 0.95</td>
          <td> 13802.070</td>
          <td> 3505</td>
          <td> 45701.725</td>
          <td> 491.47</td>
        </tr>
        <tr>
          <th>2014-12-29 00:07:00-08:00</th>
          <td> 43568.003</td>
          <td> 29.26</td>
          <td> 0.94</td>
          <td> 13802.155</td>
          <td> 3505</td>
          <td> 45701.973</td>
          <td> 491.81</td>
        </tr>
        <tr>
          <th>2014-12-29 00:08:00-08:00</th>
          <td> 43568.240</td>
          <td> 29.28</td>
          <td> 0.93</td>
          <td> 13802.239</td>
          <td> 3505</td>
          <td> 45702.224</td>
          <td> 491.52</td>
        </tr>
        <tr>
          <th>2014-12-29 00:09:00-08:00</th>
          <td> 43568.476</td>
          <td> 29.26</td>
          <td> 0.94</td>
          <td> 13802.324</td>
          <td> 3505</td>
          <td> 45702.476</td>
          <td> 491.98</td>
        </tr>
        <tr>
          <th>2014-12-29 00:10:00-08:00</th>
          <td> 43568.717</td>
          <td> 29.23</td>
          <td> 0.95</td>
          <td> 13802.402</td>
          <td> 3505</td>
          <td> 45702.728</td>
          <td> 492.01</td>
        </tr>
        <tr>
          <th>2014-12-29 00:11:00-08:00</th>
          <td> 43568.936</td>
          <td> 25.97</td>
          <td> 0.95</td>
          <td> 13802.472</td>
          <td> 3505</td>
          <td> 45702.958</td>
          <td> 492.37</td>
        </tr>
        <tr>
          <th>2014-12-29 00:12:00-08:00</th>
          <td> 43569.151</td>
          <td> 26.59</td>
          <td> 0.95</td>
          <td> 13802.536</td>
          <td> 3505</td>
          <td> 45703.183</td>
          <td> 492.63</td>
        </tr>
        <tr>
          <th>2014-12-29 00:13:00-08:00</th>
          <td> 43569.370</td>
          <td> 25.85</td>
          <td> 0.95</td>
          <td> 13802.599</td>
          <td> 3505</td>
          <td> 45703.410</td>
          <td> 490.76</td>
        </tr>
        <tr>
          <th>2014-12-29 00:14:00-08:00</th>
          <td> 43569.586</td>
          <td> 26.96</td>
          <td> 0.96</td>
          <td> 13802.665</td>
          <td> 3505</td>
          <td> 45703.636</td>
          <td> 491.22</td>
        </tr>
        <tr>
          <th>2014-12-29 00:15:00-08:00</th>
          <td> 43569.804</td>
          <td> 26.86</td>
          <td> 0.95</td>
          <td> 13802.731</td>
          <td> 3505</td>
          <td> 45703.864</td>
          <td> 490.99</td>
        </tr>
        <tr>
          <th>2014-12-29 00:16:00-08:00</th>
          <td> 43570.026</td>
          <td> 26.56</td>
          <td> 0.94</td>
          <td> 13802.797</td>
          <td> 3505</td>
          <td> 45704.095</td>
          <td> 490.65</td>
        </tr>
        <tr>
          <th>2014-12-29 00:17:00-08:00</th>
          <td> 43570.246</td>
          <td> 28.26</td>
          <td> 0.93</td>
          <td> 13802.865</td>
          <td> 3505</td>
          <td> 45704.326</td>
          <td> 490.60</td>
        </tr>
        <tr>
          <th>2014-12-29 00:18:00-08:00</th>
          <td> 43570.475</td>
          <td> 27.90</td>
          <td> 0.94</td>
          <td> 13802.945</td>
          <td> 3505</td>
          <td> 45704.569</td>
          <td> 490.77</td>
        </tr>
        <tr>
          <th>2014-12-29 00:19:00-08:00</th>
          <td> 43570.712</td>
          <td> 29.30</td>
          <td> 0.93</td>
          <td> 13803.034</td>
          <td> 3505</td>
          <td> 45704.822</td>
          <td> 490.66</td>
        </tr>
        <tr>
          <th>2014-12-29 00:20:00-08:00</th>
          <td> 43570.945</td>
          <td> 29.49</td>
          <td> 0.93</td>
          <td> 13803.125</td>
          <td> 3505</td>
          <td> 45705.071</td>
          <td> 491.08</td>
        </tr>
        <tr>
          <th>2014-12-29 00:21:00-08:00</th>
          <td> 43571.181</td>
          <td> 29.38</td>
          <td> 0.93</td>
          <td> 13803.217</td>
          <td> 3505</td>
          <td> 45705.324</td>
          <td> 490.61</td>
        </tr>
        <tr>
          <th>2014-12-29 00:22:00-08:00</th>
          <td> 43571.426</td>
          <td> 31.81</td>
          <td> 0.94</td>
          <td> 13803.308</td>
          <td> 3505</td>
          <td> 45705.585</td>
          <td> 490.40</td>
        </tr>
        <tr>
          <th>2014-12-29 00:23:00-08:00</th>
          <td> 43571.685</td>
          <td> 30.86</td>
          <td> 0.95</td>
          <td> 13803.392</td>
          <td> 3505</td>
          <td> 45705.857</td>
          <td> 490.64</td>
        </tr>
        <tr>
          <th>2014-12-29 00:24:00-08:00</th>
          <td> 43571.938</td>
          <td> 30.43</td>
          <td> 0.94</td>
          <td> 13803.477</td>
          <td> 3505</td>
          <td> 45706.124</td>
          <td> 490.87</td>
        </tr>
        <tr>
          <th>2014-12-29 00:25:00-08:00</th>
          <td> 43572.173</td>
          <td> 28.10</td>
          <td> 0.94</td>
          <td> 13803.559</td>
          <td> 3505</td>
          <td> 45706.373</td>
          <td> 490.80</td>
        </tr>
        <tr>
          <th>2014-12-29 00:26:00-08:00</th>
          <td> 43572.402</td>
          <td> 28.58</td>
          <td> 0.96</td>
          <td> 13803.637</td>
          <td> 3505</td>
          <td> 45706.614</td>
          <td> 490.89</td>
        </tr>
        <tr>
          <th>2014-12-29 00:27:00-08:00</th>
          <td> 43572.631</td>
          <td> 27.97</td>
          <td> 0.94</td>
          <td> 13803.714</td>
          <td> 3505</td>
          <td> 45706.856</td>
          <td> 490.99</td>
        </tr>
        <tr>
          <th>2014-12-29 00:28:00-08:00</th>
          <td> 43572.858</td>
          <td> 27.82</td>
          <td> 0.95</td>
          <td> 13803.792</td>
          <td> 3505</td>
          <td> 45707.096</td>
          <td> 490.49</td>
        </tr>
        <tr>
          <th>2014-12-29 00:29:00-08:00</th>
          <td> 43573.084</td>
          <td> 28.06</td>
          <td> 0.95</td>
          <td> 13803.866</td>
          <td> 3505</td>
          <td> 45707.334</td>
          <td> 491.16</td>
        </tr>
        <tr>
          <th>2014-12-29 00:30:00-08:00</th>
          <td> 43573.310</td>
          <td> 27.53</td>
          <td> 0.95</td>
          <td> 13803.942</td>
          <td> 3505</td>
          <td> 45707.572</td>
          <td> 491.15</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2015-01-28 23:31:00-08:00</th>
          <td> 53782.773</td>
          <td> 27.42</td>
          <td> 0.94</td>
          <td> 16927.487</td>
          <td> 3505</td>
          <td> 56383.743</td>
          <td> 489.66</td>
        </tr>
        <tr>
          <th>2015-01-28 23:32:00-08:00</th>
          <td> 53782.996</td>
          <td> 26.55</td>
          <td> 0.95</td>
          <td> 16927.557</td>
          <td> 3505</td>
          <td> 56383.976</td>
          <td> 489.53</td>
        </tr>
        <tr>
          <th>2015-01-28 23:33:00-08:00</th>
          <td> 53783.216</td>
          <td> 27.93</td>
          <td> 0.97</td>
          <td> 16927.621</td>
          <td> 3505</td>
          <td> 56384.206</td>
          <td> 490.18</td>
        </tr>
        <tr>
          <th>2015-01-28 23:34:00-08:00</th>
          <td> 53783.449</td>
          <td> 27.98</td>
          <td> 0.96</td>
          <td> 16927.678</td>
          <td> 3505</td>
          <td> 56384.445</td>
          <td> 490.77</td>
        </tr>
        <tr>
          <th>2015-01-28 23:35:00-08:00</th>
          <td> 53783.679</td>
          <td> 27.35</td>
          <td> 0.97</td>
          <td> 16927.737</td>
          <td> 3505</td>
          <td> 56384.682</td>
          <td> 490.35</td>
        </tr>
        <tr>
          <th>2015-01-28 23:36:00-08:00</th>
          <td> 53783.895</td>
          <td> 25.65</td>
          <td> 0.96</td>
          <td> 16927.799</td>
          <td> 3505</td>
          <td> 56384.907</td>
          <td> 490.24</td>
        </tr>
        <tr>
          <th>2015-01-28 23:37:00-08:00</th>
          <td> 53784.103</td>
          <td> 24.92</td>
          <td> 0.95</td>
          <td> 16927.861</td>
          <td> 3505</td>
          <td> 56385.124</td>
          <td> 490.48</td>
        </tr>
        <tr>
          <th>2015-01-28 23:38:00-08:00</th>
          <td> 53784.308</td>
          <td> 25.26</td>
          <td> 0.96</td>
          <td> 16927.923</td>
          <td> 3505</td>
          <td> 56385.338</td>
          <td> 490.23</td>
        </tr>
        <tr>
          <th>2015-01-28 23:39:00-08:00</th>
          <td> 53784.514</td>
          <td> 24.96</td>
          <td> 0.95</td>
          <td> 16927.982</td>
          <td> 3505</td>
          <td> 56385.552</td>
          <td> 490.43</td>
        </tr>
        <tr>
          <th>2015-01-28 23:40:00-08:00</th>
          <td> 53784.722</td>
          <td> 25.30</td>
          <td> 0.96</td>
          <td> 16928.042</td>
          <td> 3505</td>
          <td> 56385.769</td>
          <td> 490.56</td>
        </tr>
        <tr>
          <th>2015-01-28 23:41:00-08:00</th>
          <td> 53784.930</td>
          <td> 26.20</td>
          <td> 0.94</td>
          <td> 16928.102</td>
          <td> 3505</td>
          <td> 56385.985</td>
          <td> 490.61</td>
        </tr>
        <tr>
          <th>2015-01-28 23:42:00-08:00</th>
          <td> 53785.146</td>
          <td> 26.40</td>
          <td> 0.95</td>
          <td> 16928.173</td>
          <td> 3505</td>
          <td> 56386.212</td>
          <td> 490.36</td>
        </tr>
        <tr>
          <th>2015-01-28 23:43:00-08:00</th>
          <td> 53785.357</td>
          <td> 26.02</td>
          <td> 0.95</td>
          <td> 16928.244</td>
          <td> 3505</td>
          <td> 56386.435</td>
          <td> 491.07</td>
        </tr>
        <tr>
          <th>2015-01-28 23:44:00-08:00</th>
          <td> 53785.570</td>
          <td> 25.33</td>
          <td> 0.95</td>
          <td> 16928.315</td>
          <td> 3505</td>
          <td> 56386.660</td>
          <td> 490.87</td>
        </tr>
        <tr>
          <th>2015-01-28 23:45:00-08:00</th>
          <td> 53785.777</td>
          <td> 27.96</td>
          <td> 0.95</td>
          <td> 16928.385</td>
          <td> 3505</td>
          <td> 56386.879</td>
          <td> 489.09</td>
        </tr>
        <tr>
          <th>2015-01-28 23:46:00-08:00</th>
          <td> 53785.990</td>
          <td> 25.64</td>
          <td> 0.95</td>
          <td> 16928.453</td>
          <td> 3505</td>
          <td> 56387.102</td>
          <td> 488.35</td>
        </tr>
        <tr>
          <th>2015-01-28 23:47:00-08:00</th>
          <td> 53786.199</td>
          <td> 25.72</td>
          <td> 0.95</td>
          <td> 16928.521</td>
          <td> 3505</td>
          <td> 56387.322</td>
          <td> 488.43</td>
        </tr>
        <tr>
          <th>2015-01-28 23:48:00-08:00</th>
          <td> 53786.406</td>
          <td> 24.65</td>
          <td> 0.96</td>
          <td> 16928.583</td>
          <td> 3505</td>
          <td> 56387.538</td>
          <td> 488.01</td>
        </tr>
        <tr>
          <th>2015-01-28 23:49:00-08:00</th>
          <td> 53786.610</td>
          <td> 24.82</td>
          <td> 0.96</td>
          <td> 16928.643</td>
          <td> 3505</td>
          <td> 56387.750</td>
          <td> 490.34</td>
        </tr>
        <tr>
          <th>2015-01-28 23:50:00-08:00</th>
          <td> 53786.817</td>
          <td> 24.67</td>
          <td> 0.96</td>
          <td> 16928.703</td>
          <td> 3505</td>
          <td> 56387.966</td>
          <td> 490.90</td>
        </tr>
        <tr>
          <th>2015-01-28 23:51:00-08:00</th>
          <td> 53787.026</td>
          <td> 26.07</td>
          <td> 0.97</td>
          <td> 16928.762</td>
          <td> 3505</td>
          <td> 56388.183</td>
          <td> 491.24</td>
        </tr>
        <tr>
          <th>2015-01-28 23:52:00-08:00</th>
          <td> 53787.242</td>
          <td> 26.13</td>
          <td> 0.96</td>
          <td> 16928.822</td>
          <td> 3505</td>
          <td> 56388.407</td>
          <td> 491.19</td>
        </tr>
        <tr>
          <th>2015-01-28 23:53:00-08:00</th>
          <td> 53787.457</td>
          <td> 26.34</td>
          <td> 0.96</td>
          <td> 16928.881</td>
          <td> 3505</td>
          <td> 56388.630</td>
          <td> 491.38</td>
        </tr>
        <tr>
          <th>2015-01-28 23:54:00-08:00</th>
          <td> 53787.672</td>
          <td> 25.28</td>
          <td> 0.96</td>
          <td> 16928.940</td>
          <td> 3505</td>
          <td> 56388.852</td>
          <td> 490.93</td>
        </tr>
        <tr>
          <th>2015-01-28 23:55:00-08:00</th>
          <td> 53787.883</td>
          <td> 25.70</td>
          <td> 0.96</td>
          <td> 16928.999</td>
          <td> 3505</td>
          <td> 56389.072</td>
          <td> 488.62</td>
        </tr>
        <tr>
          <th>2015-01-28 23:56:00-08:00</th>
          <td> 53788.088</td>
          <td> 24.37</td>
          <td> 0.97</td>
          <td> 16929.057</td>
          <td> 3505</td>
          <td> 56389.285</td>
          <td> 488.23</td>
        </tr>
        <tr>
          <th>2015-01-28 23:57:00-08:00</th>
          <td> 53788.287</td>
          <td> 24.31</td>
          <td> 0.98</td>
          <td> 16929.107</td>
          <td> 3505</td>
          <td> 56389.489</td>
          <td> 488.86</td>
        </tr>
        <tr>
          <th>2015-01-28 23:58:00-08:00</th>
          <td> 53788.493</td>
          <td> 24.84</td>
          <td> 0.97</td>
          <td> 16929.161</td>
          <td> 3505</td>
          <td> 56389.702</td>
          <td> 488.96</td>
        </tr>
        <tr>
          <th>2015-01-28 23:59:00-08:00</th>
          <td> 53788.692</td>
          <td> 23.47</td>
          <td> 0.96</td>
          <td> 16929.215</td>
          <td> 3505</td>
          <td> 56389.908</td>
          <td> 489.18</td>
        </tr>
        <tr>
          <th>2015-01-29 00:00:00-08:00</th>
          <td> 53788.890</td>
          <td> 25.48</td>
          <td> 0.96</td>
          <td> 16929.271</td>
          <td> 3505</td>
          <td> 56390.113</td>
          <td> 489.14</td>
        </tr>
      </tbody>
    </table>
    <p>44640 rows × 7 columns</p>
    </div>



                
``search_group_tree`` accepts a keyword and searches the instantiated client for matching sensor groups returning group names, sensor group ID, and assigned sensors.

                
.. code:: python

    stream.search_group_tree('Engineering', case = False)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>description</th>
          <th>load_type</th>
          <th>sensorGroups</th>
          <th>sensors</th>
          <th>groupMultiplier</th>
          <th>time_zone</th>
          <th>weatherStationId</th>
          <th>base_group_level</th>
        </tr>
        <tr>
          <th>sensorGroupId</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>157</th>
          <td>      Engineering Laboratory Facility - Sub Groups</td>
          <td>                             Feed to ELF Sub Loads</td>
          <td> building</td>
          <td> Int64Index([196, 193, 192, 195, 194], dtype='i...</td>
          <td>                                              None</td>
          <td>             [1, 1, 1, 1, 1]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>255</th>
          <td>                    Engineering Tower - Sub Groups</td>
          <td>                             Feed to ET Sub Groups</td>
          <td> building</td>
          <td> Int64Index([258, 256, 257, 262, 263, 260, 261,...</td>
          <td>                                              None</td>
          <td> [1, 1, 1, 1, 1, 1, 1, 1, 1]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>265</th>
          <td>             Engineering Lecture Hall - Sub Groups</td>
          <td>                              Feed ELH Sub Groups </td>
          <td> building</td>
          <td> Int64Index([274, 266, 271, 267, 270, 273, 272]...</td>
          <td>                                              None</td>
          <td>       [1, 1, 1, 3, 3, 3, 3]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>221</th>
          <td> Engineering Laboratory Facility - Main Switchb...</td>
          <td>                                 Feed to ELF - MSB</td>
          <td> building</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>254</th>
          <td>              Engineering Tower - Main Switchboard</td>
          <td>                         Feed to Engineering Tower</td>
          <td> building</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>264</th>
          <td>       Engineering Lecture Hall - Main Switchboard</td>
          <td>                                       Feed to ELH</td>
          <td> building</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td>   1</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>364</th>
          <td>              Engineering Lecture Hall - 3rd Party</td>
          <td>     PowerLogic ION7300 Electrical Building Meter </td>
          <td> building</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 2, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>363</th>
          <td>                   Engineering Gateway - 3rd Party</td>
          <td> PowerLogic ION8600 (2) and PowerLogic ION7300 ...</td>
          <td>   campus</td>
          <td>        Int64Index([381, 382, 362], dtype='int64')</td>
          <td>                                              None</td>
          <td>                   [1, 1, 1]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>728</th>
          <td>                      Engineering Hall - 3rd Party</td>
          <td>            Siemens 9330 Electrical Building Meter</td>
          <td> building</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 2, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>381</th>
          <td>                 Engineering Gateway B - 3rd Party</td>
          <td>                                PowerLogic ION8600</td>
          <td>    floor</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 2, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 3</td>
        </tr>
        <tr>
          <th>382</th>
          <td>                 Engineering Gateway A - 3rd Party</td>
          <td>                                PowerLogic ION8600</td>
          <td>    floor</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 2, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 3</td>
        </tr>
        <tr>
          <th>362</th>
          <td>                 Engineering Gateway C - 3rd Party</td>
          <td>      PowerLogic ION7300 Electrical Building Meter</td>
          <td>    floor</td>
          <td>                                              None</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 2, u'des...</td>
          <td>                        None</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 3</td>
        </tr>
      </tbody>
    </table>
    </div>



                
Sensors are grouped in a heirarchy by level.

                
.. code:: python

    stream.groups[stream.groups.base_group_level == 0]



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>description</th>
          <th>load_type</th>
          <th>sensorGroups</th>
          <th>sensors</th>
          <th>groupMultiplier</th>
          <th>time_zone</th>
          <th>weatherStationId</th>
          <th>base_group_level</th>
        </tr>
        <tr>
          <th>sensorGroupId</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>216 </th>
          <td>          UCI - MelRok Electric Meter Sub Groups</td>
          <td>         Feed to Individual Loads at UCI Buildings</td>
          <td> campus</td>
          <td> Int64Index([1039, 137, 139, 128, 157, 158, 159...</td>
          <td> None</td>
          <td> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 0</td>
        </tr>
        <tr>
          <th>734 </th>
          <td>               UCI - Electric Distribution Loads</td>
          <td> Electrical Meters that Distribute Electricity ...</td>
          <td> campus</td>
          <td> Int64Index([732, 733, 1836, 1837, 1838, 1839, ...</td>
          <td> None</td>
          <td>                      [1, 1, 1, 1, 1, 1, -1, 1, 1]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 0</td>
        </tr>
        <tr>
          <th>769 </th>
          <td> UCI - Building Hot and Chilled Water BTU Meters</td>
          <td>                      14 KEP-ES749 for 6 Buildings</td>
          <td> campus</td>
          <td> Int64Index([774, 775, 772, 771, 776, 777, 1824...</td>
          <td> None</td>
          <td>                       [1, 1, 1, 1, 1, 1, 1, 1, 1]</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 0</td>
        </tr>
        <tr>
          <th>1843</th>
          <td>                       UCI - Total Electric Load</td>
          <td>                Total Electric Load for UCI Campus</td>
          <td> campus</td>
          <td> Int64Index([735, 1842, 1484, 1483, 1486, 1485,...</td>
          <td> None</td>
          <td> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...</td>
          <td> America/Los_Angeles</td>
          <td> 102</td>
          <td> 0</td>
        </tr>
      </tbody>
    </table>
    </div>



                
``sensors`` returns a dataframe describing the individual sensors associated with the instantiated energistream client ID. This includes the sensor ID, the associated group ID, time zone, and a multiplier based on the method of measurement i.e. one, two, or three channel.

                
.. code:: python

    stream.sensors



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>iconId</th>
          <th>multiplier</th>
          <th>name</th>
          <th>properties</th>
          <th>sensorFunctionTypeId</th>
          <th>sensorGroupId</th>
          <th>sourceTypeId</th>
          <th>time_zone</th>
        </tr>
        <tr>
          <th>sensorId</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>3505</th>
          <td> A40006000305-01</td>
          <td> 21</td>
          <td> 1</td>
          <td>                        HH DP3</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1044</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3506</th>
          <td> A40006000305-02</td>
          <td> 21</td>
          <td> 1</td>
          <td>                        HH DP3</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1044</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3490</th>
          <td> A40006000302-10</td>
          <td> 21</td>
          <td> 1</td>
          <td>                   HH ELDP EM3</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1057</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3491</th>
          <td> A40006000302-11</td>
          <td> 21</td>
          <td> 1</td>
          <td>                   HH ELDP EM3</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1057</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3492</th>
          <td> A40006000302-12</td>
          <td> 21</td>
          <td> 1</td>
          <td>                   HH ELDP EM3</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1057</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3466</th>
          <td> A40006000296-10</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH HLP3</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1043</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3467</th>
          <td> A40006000296-11</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH HLP3</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1043</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3468</th>
          <td> A40006000296-12</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH HLP3</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1043</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3989</th>
          <td> A40007000015-05</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH HWB-1</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1062</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3990</th>
          <td> A40007000015-06</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH HWB-1</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1062</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3997</th>
          <td> A40007000015-13</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH AH-2</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1070</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3998</th>
          <td> A40007000015-14</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH AH-2</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1070</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3991</th>
          <td> A40007000015-07</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH AH-3R</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1071</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3992</th>
          <td> A40007000015-08</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH AH-3R</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1071</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4007</th>
          <td> A40007000015-23</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH AH-1</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1069</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4008</th>
          <td> A40007000015-24</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH AH-1</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1069</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4005</th>
          <td> A40007000015-21</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH AH-3S</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1072</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4006</th>
          <td> A40007000015-22</td>
          <td> 21</td>
          <td> 1</td>
          <td>                      HH AH-3S</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1072</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3985</th>
          <td> A40007000015-01</td>
          <td> 21</td>
          <td> 1</td>
          <td>                         HH P1</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1059</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3986</th>
          <td> A40007000015-02</td>
          <td> 21</td>
          <td> 1</td>
          <td>                         HH P1</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1059</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3987</th>
          <td> A40007000015-03</td>
          <td> 21</td>
          <td> 1</td>
          <td>                         HH P2</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1060</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3988</th>
          <td> A40007000015-04</td>
          <td> 21</td>
          <td> 1</td>
          <td>                         HH P2</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1060</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3993</th>
          <td> A40007000015-09</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-4</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1066</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3994</th>
          <td> A40007000015-10</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-4</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1066</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3995</th>
          <td> A40007000015-11</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-5</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1067</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>3996</th>
          <td> A40007000015-12</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-5</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1067</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4001</th>
          <td> A40007000015-17</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-2</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1064</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4002</th>
          <td> A40007000015-18</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-2</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1064</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4003</th>
          <td> A40007000015-19</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-3</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1065</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>4004</th>
          <td> A40007000015-20</td>
          <td> 21</td>
          <td> 1</td>
          <td>                       HH EF-3</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1065</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>5242</th>
          <td> A40006000224-10</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 5</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1892</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5243</th>
          <td> A40006000224-11</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 6</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1892</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5244</th>
          <td> A40006000224-12</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 6</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1892</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5235</th>
          <td> A40006000224-03</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 2</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1887</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5236</th>
          <td> A40006000224-04</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 2</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1887</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5233</th>
          <td> A40006000224-01</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 1</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1886</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5234</th>
          <td> A40006000224-02</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 1</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1886</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5241</th>
          <td> A40006000224-09</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 5</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1890</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5242</th>
          <td> A40006000224-10</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 5</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1890</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5243</th>
          <td> A40006000224-11</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 6</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1891</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5244</th>
          <td> A40006000224-12</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 6</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1891</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5237</th>
          <td> A40006000224-05</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 3</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1888</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5238</th>
          <td> A40006000224-06</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 3</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1888</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5239</th>
          <td> A40006000224-07</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 4</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1889</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>5240</th>
          <td> A40006000224-08</td>
          <td> 21</td>
          <td> 1</td>
          <td>               Charging Port 4</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1889</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7240</th>
          <td> B40011000568-04</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Parking Structure Panel H/HA</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1859</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7241</th>
          <td> B40011000568-05</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Parking Structure Panel H/HA</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1859</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7242</th>
          <td> B40011000568-06</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Parking Structure Panel H/HA</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1859</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7245</th>
          <td> B40011000568-09</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Mesa Arts Building Panel MSM</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1856</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7244</th>
          <td> B40011000568-08</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Mesa Arts Building Panel MSM</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1855</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7243</th>
          <td> B40011000568-07</td>
          <td> 21</td>
          <td> 1</td>
          <td>  Mesa Arts Building Panel MSM</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1854</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7249</th>
          <td> B40011000568-13</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 2L</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1851</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7250</th>
          <td> B40011000568-14</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 2L</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1851</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7251</th>
          <td> B40011000568-15</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 2L</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1851</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7246</th>
          <td> B40011000568-10</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 1L</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1850</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7247</th>
          <td> B40011000568-11</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 1L</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1850</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>7248</th>
          <td> B40011000568-12</td>
          <td> 21</td>
          <td> 1</td>
          <td> Mesa Office Building Panel 1L</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1850</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>775 </th>
          <td> B30007000030-07</td>
          <td> 21</td>
          <td> 1</td>
          <td>               SC1 C.C. Center</td>
          <td> [{u'name': u'Phase', u'value': u'A'}]</td>
          <td> 1</td>
          <td> 1123</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>776 </th>
          <td> B30007000030-08</td>
          <td> 21</td>
          <td> 1</td>
          <td>               SC1 C.C. Center</td>
          <td> [{u'name': u'Phase', u'value': u'B'}]</td>
          <td> 1</td>
          <td> 1123</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
        <tr>
          <th>777 </th>
          <td> B30007000030-09</td>
          <td> 21</td>
          <td> 1</td>
          <td>               SC1 C.C. Center</td>
          <td> [{u'name': u'Phase', u'value': u'C'}]</td>
          <td> 1</td>
          <td> 1123</td>
          <td> 1</td>
          <td> America/Los_Angeles</td>
        </tr>
      </tbody>
    </table>
    <p>1713 rows × 9 columns</p>
    </div>



                
``get_boards`` returns a dataframe describing the boards associated with the instantiated energistream client ID. This includes 
the boards serial number, version, display name, and model.

                
.. code:: python

    stream.get_boards 



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>currentConfigVersion</th>
          <th>displayName</th>
          <th>firmwareVersion</th>
          <th>manufacturer</th>
          <th>model</th>
          <th>sensors</th>
          <th>timeZoneId</th>
        </tr>
        <tr>
          <th>serialNumber</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>C20006000002</th>
          <td> 26</td>
          <td>                       MSTB First Floor 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>C20006000003</th>
          <td> 21</td>
          <td>                       MSTB First Floor 3</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>C20006000004</th>
          <td> 25</td>
          <td>                        MSTB Second Floor</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000036</th>
          <td> 20</td>
          <td>                             Aldrich Hall</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000041</th>
          <td> 18</td>
          <td>                       Social Science LAB</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000047</th>
          <td> 17</td>
          <td>                        Langson Library 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000051</th>
          <td> 18</td>
          <td>                     Social Science Tower</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000053</th>
          <td> 30</td>
          <td>                          Humanities Hall</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000054</th>
          <td> 49</td>
          <td>                 Engineering Lab Facility</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000055</th>
          <td> 19</td>
          <td>                                     AIRB</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30007000007</th>
          <td> 25</td>
          <td>          Medical Sciences Building D - 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30007000008</th>
          <td> 15</td>
          <td>          Medical Sciences Building D - 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30007000009</th>
          <td> 15</td>
          <td>          Medical Sciences Building C - 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30007000010</th>
          <td> 15</td>
          <td>          Medical Sciences Building C - 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30007000012</th>
          <td> 23</td>
          <td>                     Social Science Plaza</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30006000046</th>
          <td> 17</td>
          <td>                            Reines Hall 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30006000058</th>
          <td> 19</td>
          <td>                              Vista Field</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000030</th>
          <td> 27</td>
          <td>                         Student Center 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000035</th>
          <td> 22</td>
          <td>                            Reines Hall 4</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000036</th>
          <td> 22</td>
          <td>                            Reines Hall 3</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000037</th>
          <td> 20</td>
          <td>                            Reines Hall 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000039</th>
          <td> 22</td>
          <td>               Bonney Research Laboratory</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30006000044</th>
          <td> 21</td>
          <td>       Intercollegiate Athletics Building</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30006000052</th>
          <td> 19</td>
          <td>                         Social Ecology 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30006000049</th>
          <td> 18</td>
          <td>                                    ARC 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000014</th>
          <td> 24</td>
          <td>                                    ARC 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>C30007000033</th>
          <td> 21</td>
          <td>                         Irvine Hall East</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>C30006000100</th>
          <td> 16</td>
          <td>                         Irvine Hall West</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B30007000034</th>
          <td> 21</td>
          <td>                         Student Center 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A30006000026</th>
          <td> 16</td>
          <td>          Medical Sciences Building C - 3</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>A40007000089</th>
          <td>  9</td>
          <td>              Campus Village T-69 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40007000087</th>
          <td>  9</td>
          <td>              Campus Village T-70 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000224</th>
          <td> 11</td>
          <td> Lot 16 Electric Vehicle Charging Station</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40008000001</th>
          <td>  3</td>
          <td>                   Aldrich Hall - Control</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td> T-PCRS485-R4-WM</td>
          <td>                                                []</td>
          <td> 24</td>
        </tr>
        <tr>
          <th>B40008000002</th>
          <td>  3</td>
          <td>     Anteater Recreation Center - Control</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td> T-PCRS485-R4-WM</td>
          <td>                                                []</td>
          <td> 24</td>
        </tr>
        <tr>
          <th>B40008000003</th>
          <td>  3</td>
          <td>          Berkeley Place Campus - Control</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td> T-PCRS485-R4-WM</td>
          <td>                                                []</td>
          <td> 24</td>
        </tr>
        <tr>
          <th>A40006000227</th>
          <td> 12</td>
          <td>                            MCC-3 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000226</th>
          <td> 12</td>
          <td>                            MCC-5 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000318</th>
          <td> 14</td>
          <td>                       MCC-CTG-01 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000502</th>
          <td>  9</td>
          <td>                        Verano Place T-36</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000503</th>
          <td> 10</td>
          <td>                        Verano Place T-37</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000504</th>
          <td>  9</td>
          <td>              Campus Village T-70 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000316</th>
          <td> 13</td>
          <td>                        SWGR T-61 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000324</th>
          <td> 10</td>
          <td>                   Social Science Trailer</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000524</th>
          <td>  9</td>
          <td>                                  MCC-CHC</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000525</th>
          <td> 14</td>
          <td>                                  SWGR T3</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000530</th>
          <td> 10</td>
          <td>                            MCC-5 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000532</th>
          <td>  8</td>
          <td>                            MCC-3 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000531</th>
          <td> 12</td>
          <td>                                  SWGR T2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000538</th>
          <td> 12</td>
          <td>                        SWGR T-61 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000546</th>
          <td> 24</td>
          <td>                                    MCC-7</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000535</th>
          <td> 10</td>
          <td>                                    MCC-8</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000551</th>
          <td> 13</td>
          <td>                          Medical Surge 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000559</th>
          <td>  9</td>
          <td>                        MCC-BOP-1 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000543</th>
          <td> 11</td>
          <td>                        MCC-BOP-1 Board 2</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000566</th>
          <td>  8</td>
          <td>                       MCC-CTG-01 Board 1</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40011000568</th>
          <td> 10</td>
          <td>                     Mesa Office Building</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-24</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40010000502</th>
          <td> 10</td>
          <td>                     Rockwell Engineering</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>B40010000503</th>
          <td> 10</td>
          <td>                            Bison Modular</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
        <tr>
          <th>A40006000199</th>
          <td> 10</td>
          <td>                                Berk Hall</td>
          <td> 1</td>
          <td> MelRok Manufacturer</td>
          <td>           EN-12</td>
          <td> [{u'timeZoneId': 67, u'sourceTypeId': 1, u'nam...</td>
          <td> 67</td>
        </tr>
      </tbody>
    </table>
    <p>90 rows × 7 columns</p>
    </div>



                
``get_demand`` returns the fifteen minute demand rate for the given sensor group. Start and end date may be specified as well as the timezone and desired resolution. Note : Defaults to the last thirty days and fifteen minute resolution.

                
.. code:: python

    stream.get_demand(157)



.. parsed-literal::

    2014-12-29 16:14:59-08:00     23.746600
    2014-12-29 16:29:59-08:00     23.931200
    2014-12-29 16:44:59-08:00     23.828933
    2014-12-29 16:59:59-08:00     23.743933
    2014-12-29 17:14:59-08:00    147.089266
    2014-12-29 17:29:59-08:00     23.756733
    2014-12-29 17:44:59-08:00     23.642666
    2014-12-29 17:59:59-08:00     23.688866
    2014-12-29 18:14:59-08:00     23.787400
    2014-12-29 18:29:59-08:00     23.931266
    2014-12-29 18:44:59-08:00     23.857133
    2014-12-29 18:59:59-08:00     23.896533
    2014-12-29 19:14:59-08:00    145.263333
    2014-12-29 19:29:59-08:00     26.592933
    2014-12-29 19:44:59-08:00     23.813800
    ...
    2015-01-29 12:29:59-08:00    170.640600
    2015-01-29 12:44:59-08:00     47.933000
    2015-01-29 12:59:59-08:00     48.071533
    2015-01-29 13:14:59-08:00     48.101533
    2015-01-29 13:29:59-08:00    171.545800
    2015-01-29 13:44:59-08:00     48.256066
    2015-01-29 13:59:59-08:00     47.851533
    2015-01-29 14:14:59-08:00     83.046266
    2015-01-29 14:29:59-08:00    149.004600
    2015-01-29 14:44:59-08:00    152.480000
    2015-01-29 14:59:59-08:00    101.425933
    2015-01-29 15:14:59-08:00    159.006866
    2015-01-29 15:29:59-08:00    129.128666
    2015-01-29 15:44:59-08:00    104.994133
    2015-01-29 15:59:59-08:00     54.097933
    Name: kW, Length: 2976



