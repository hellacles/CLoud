import React from "react";
import axios from 'axios';
import PropTypes from "prop-types";
import {
  Row,
  Col,
  FormSelect,
  Card,
  CardHeader,
  CardBody,
  CardFooter
} from "shards-react";

import Chart from "../../utils/chart";

class UsersByDevice extends React.Component {
  constructor(props) {
    super(props);

    this.canvasRef = React.createRef();
  }

  state = {
    params: []
  }

  apiEndpoint = "https://64mg85mq2c.execute-api.us-east-1.amazonaws.com/hella/status";
  getDeliveryStatus = async () => {
    await axios.get(this.apiEndpoint).then((res) => {
        const result = res.data;
        // console.log(params)
        this.setState({params: result});
    });
  };

  componentDidMount() {
    this.getDeliveryStatus();
    setTimeout(function() {
      const chartConfig = {
        type: "pie",
        data: {
          datasets: [
            {
              hoverBorderColor: "#ffffff",
              data: [this.state.params['s0'], this.state.params['s1'], this.state.params['s2'], this.state.params['s3'], this.state.params['s4']],
              backgroundColor: [
                "rgba(0,123,255,0.9)",
                "rgba(147,204,2,0.5)",
                "rgba(2,204,130,0.3)",
                "rgba(172,172,173,0.6)",
                "rgba(204,22,2,0.7)"
              ]
            }
          ],
          labels: ["신규주문", "주문접수", "배달중", "배달완료", "주문취소"]
        },
        options: {
          ...{
            legend: {
              position: "bottom",
              labels: {
                padding: 25,
                boxWidth: 20
              }
            },
            cutoutPercentage: 0,
            tooltips: {
              custom: false,
              mode: "index",
              position: "nearest"
            }
          },
          ...this.props.chartOptions
        }
      };
      
      new Chart(this.canvasRef.current, chartConfig);
    }.bind(this), 2000)
    
  }

  render() {
    const { title } = this.props;
    return (
      <Card small className="h-100">
        <CardHeader className="border-bottom">
          <h6 className="m-0">{title}</h6>
        </CardHeader>
        <CardBody className="d-flex py-0">
          <canvas
            height="300"
            ref={this.canvasRef}
            className="blog-users-by-device m-auto"
          />
        </CardBody>
        {/* <CardFooter className="border-top">
          <Row>
            <Col>
              <FormSelect
                size="sm"
                value="last-week"
                style={{ maxWidth: "130px" }}
                onChange={() => {}}
              >
                <option value="last-week">Last Week</option>
                <option value="today">Today</option>
                <option value="last-month">Last Month</option>
                <option value="last-year">Last Year</option>
              </FormSelect>
            </Col>
            <Col className="text-right view-report">
              <a href="#">View full report &rarr;</a>
            </Col>
          </Row>
        </CardFooter> */}
      </Card>
    );
  }
}

UsersByDevice.propTypes = {
  /**
   * The component's title.
   */
  title: PropTypes.string,
  /**
   * The chart config object.
   */
  chartConfig: PropTypes.object,
  /**
   * The Chart.js options.
   */
  chartOptions: PropTypes.object,
  /**
   * The chart data.
   */
  chartData: PropTypes.object
};

UsersByDevice.defaultProps = {
  title: "배달 현황",
  chartData: {
    datasets: [
      {
        hoverBorderColor: "#ffffff",
        data: [68.3, 24.2, 7.5],
        backgroundColor: [
          "rgba(0,123,255,0.9)",
          "rgba(0,123,255,0.5)",
          "rgba(0,123,255,0.3)"
        ]
      }
    ],
    labels: ["Desktop", "Tablet", "Mobile"]
  }
};

export default UsersByDevice;
